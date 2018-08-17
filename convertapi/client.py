import requests

from .exceptions import *

class Client:
	def __init__(self, configuration):
		self.configuration = configuration

	def get(self, path, params = {}):
		r = requests.get(self.url(path), params=params, headers = self.headers())
		return self.handle_response(r)

	def post(self, path, payload):
		r = requests.post(self.url(path), json=payload, headers = self.headers())
		return self.handle_response(r)

	def handle_response(self, r):
		json = r.json()

		if r.status_code >= 400:
			raise ConvertApiError(json['Message'])

		r.raise_for_status()

		return json

	def url(self, path):
		return "%s/%s?Secret=%s" % (self.configuration.base_uri, path, self.configuration.api_secret)

	def headers(self):
		return {
			'User-Agent': self.configuration.user_agent,
		}
