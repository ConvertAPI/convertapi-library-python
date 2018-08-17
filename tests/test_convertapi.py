from . import utils
from nose.tools import eq_
import convertapi

class TestConvertapi(utils.TestCase):
	def testDefaults(self):
		eq_('https://v2.convertapi.com/', convertapi.configuration.base_uri)

	def testConfiguration(self):
		convertapi.configuration.api_secret = 'TEST'
		eq_('TEST', convertapi.client.configuration.api_secret)