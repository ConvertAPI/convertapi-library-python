import convertapi
import os
import io
import tempfile

from . import utils
from nose.tools import eq_

class TestConvertapi(utils.TestCase):
	def setUp(self):
		convertapi.api_secret = os.environ['CONVERT_API_SECRET']

	def test_defaults(self):
		eq_('https://v2.convertapi.com/', convertapi.base_uri)

	def test_configuration(self):
		convertapi.api_secret = 'TEST'
		eq_('TEST', convertapi.api_secret)

	def test_convert_file(self):
		result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' }, 'docx')
		assert result.save_files(tempfile.gettempdir())
		assert result.conversion_cost > 0

	def test_convert_url(self):
		result = convertapi.convert('pdf', { 'Url': 'http://convertapi.com' }, 'web')
		assert result.conversion_cost > 0

	def test_upload_io(self):
		string_io = io.StringIO(u'test')
		upload_io = convertapi.UploadIO(string_io, 'test.txt')
		result = convertapi.convert('pdf', { 'File': upload_io }, 'txt')
		assert result.conversion_cost > 0