import convertapi
import os
import tempfile

from . import utils
from nose.tools import eq_

class TestConvertapi(utils.TestCase):
	def setUp(self):
		convertapi.configuration.api_secret = os.environ['CONVERT_API_SECRET']

	def test_defaults(self):
		eq_('https://v2.convertapi.com/', convertapi.configuration.base_uri)

	def test_configuration(self):
		convertapi.configuration.api_secret = 'TEST'
		eq_('TEST', convertapi.client.configuration.api_secret)

	def test_convert(self):
		result = convertapi.convert('pdf', { 'Url': 'http://convertapi.com' }, 'web')
		print(result.save_files(tempfile.gettempdir()))

