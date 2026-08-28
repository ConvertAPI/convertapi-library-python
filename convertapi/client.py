import threading

import requests
import convertapi

from io import BytesIO
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import *


class Client:
	def __init__(self):
		self._session = None
		self._session_lock = threading.Lock()

	# --- session management --------------------------------------------------

	def session(self):
		"""One Session -- and therefore one connection pool -- per process."""
		if self._session is None:
			with self._session_lock:
				if self._session is None:
					self._session = self.__build_session()

		return self._session

	def close(self):
		"""Close pooled sockets. Call on worker shutdown, or after changing base_uri."""
		with self._session_lock:
			if self._session is not None:
				self._session.close()
				self._session = None

	def __build_session(self):
		s = requests.Session()

		# Retries are limited to idempotent methods on purpose: retrying
		# POST /convert after a 5xx risks paying for the same conversion twice.
		retries = Retry(
			total = convertapi.max_retries,
			backoff_factor = convertapi.retry_backoff_factor,
			status_forcelist = (429, 500, 502, 503, 504),
			respect_retry_after_header = True,
		)

		adapter = HTTPAdapter(
			pool_connections = convertapi.pool_connections,
			pool_maxsize = convertapi.pool_maxsize,
			pool_block = True,
			max_retries = retries,
		)

		s.mount('https://', adapter)
		s.mount('http://', adapter)

		s.headers.update({ 'User-Agent': convertapi.user_agent })

		return s

	def __request_kwargs(self):
		"""Auth/verify sent per request so a cached session still sees config changes."""
		return {
			'headers': { 'Authorization': 'Bearer ' + convertapi.api_credentials },
			'verify': convertapi.verify_ssl,
		}

	# --- requests ------------------------------------------------------------

	def get(self, path, params = {}, timeout = None):
		url = self.__url(path)
		timeout = timeout or convertapi.timeout

		with self.session().get(url, params = params, timeout = timeout,
				**self.__request_kwargs()) as r:
			return self.__handle_response(r)

	def post(self, path, payload, timeout = None):
		url = self.__url(path)
		timeout = timeout or convertapi.timeout

		with self.session().post(url, data = payload, timeout = timeout,
				**self.__request_kwargs()) as r:
			return self.__handle_response(r)

	def upload(self, io, filename):
		url = convertapi.base_uri + 'upload'
		encoded_filename = requests.utils.quote(filename)

		kwargs = self.__request_kwargs()
		kwargs['headers']['Content-Disposition'] = \
			"attachment; filename*=UTF-8''" + encoded_filename

		with self.session().post(url, data = io,
				timeout = convertapi.upload_timeout, **kwargs) as r:
			return self.__handle_response(r)

	def download(self, url, path):
		with self.session().get(url, stream = True,
				timeout = convertapi.download_timeout,
				**self.__request_kwargs()) as r:
			r.raise_for_status()

			with open(path, 'wb') as f:
				for chunk in r.iter_content(chunk_size = 64 * 1024):
					if chunk:
						f.write(chunk)

		return path

	def download_io(self, url):
		with self.session().get(url, timeout = convertapi.download_timeout,
				**self.__request_kwargs()) as r:
			r.raise_for_status()
			return BytesIO(r.content)

	# --- helpers -------------------------------------------------------------

	def __handle_response(self, r):
		try:
			r.raise_for_status()
		except requests.RequestException as e:
			try:
				raise ApiError(r.json())
			except ValueError:
				raise e

		return r.json()

	def __url(self, path):
		return convertapi.base_uri + path
