import requests
import convertapi

from io import BytesIO
from .exceptions import *

class Client:
	def get(self, path, params = {}, timeout = None):
		url = self.__url(path)
		timeout = timeout or convertapi.timeout
		r = self.__session().get(url, params = params, timeout = timeout)
		return self.__handle_response(r)

	def post(self, path, payload, timeout = None):
		url = self.__url(path)
		timeout = timeout or convertapi.timeout
		r = self.__session().post(url, data = payload, timeout = timeout)
		return self.__handle_response(r)

	def upload(self, io, filename):
		url = convertapi.base_uri + 'upload'
		encoded_filename = requests.utils.quote(filename)

		headers = {
			'Content-Disposition': "attachment; filename*=UTF-8''" + encoded_filename,
		}

		r = self.__session().post(url, data = io, headers = headers, timeout = convertapi.upload_timeout)
		return self.__handle_response(r)

	def download(self, url, path):
		r = self.__session().get(url, stream = True, timeout = convertapi.download_timeout)

		with open(path, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024):
				if chunk:
					f.write(chunk)

		return path

	def download_io(self, url):
		response = self.__session().get(url, timeout = convertapi.download_timeout)
		return BytesIO(response.content)

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
		return "%s%s?Secret=%s" % (convertapi.base_uri, path, convertapi.api_secret)

	def __session(self):
		s = requests.Session()
		s.headers.update({ 'User-Agent': convertapi.user_agent })
		s.verify = convertapi.verify_ssl

		return s
