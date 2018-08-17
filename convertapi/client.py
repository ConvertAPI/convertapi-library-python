import requests

from .exceptions import *

class Client:
	def __init__(self, configuration):
		self.configuration = configuration

	def get(self, path, params = {}, timeout = None):
		timeout = timeout or self.configuration.timeout
		r = requests.get(self.url(path), params = params, headers = self.headers(), timeout = timeout)
		return self.handle_response(r)

	def post(self, path, payload, timeout = None):
		timeout = timeout or self.configuration.timeout
		r = requests.post(self.url(path), data = payload, headers = self.headers(), timeout = timeout)
		return self.handle_response(r)

	def download(self, url, path):
		r = requests.get(url, stream = True, timeout = self.configuration.download_timeout)

		with open(path, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024):
				if chunk:
					f.write(chunk)

		return path

	def handle_response(self, r):
		json = r.json()

		if r.status_code >= 400:
			raise ConvertApiError(json['Message'])

		r.raise_for_status()

		return json

	def url(self, path):
		return "%s%s?Secret=%s" % (self.configuration.base_uri, path, self.configuration.api_secret)

	def headers(self):
		return {
			'User-Agent': self.configuration.user_agent,
		}
