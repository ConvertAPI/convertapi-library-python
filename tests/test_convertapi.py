import convertapi
import os
import io
import tempfile
import requests
import responses

from . import utils
from nose.tools import *

class TestConvertapi(utils.TestCase):
	def setUp(self):
		convertapi.api_secret = os.environ['CONVERT_API_SECRET']
		convertapi.api_key = None
		convertapi.api_token = None
		convertapi.max_parallel_uploads = 10

	def test_defaults(self):
		eq_('https://v2.convertapi.com/', convertapi.base_uri)

	def test_configuration(self):
		convertapi.api_secret = 'TEST'
		eq_('TEST', convertapi.api_secret)

	def test_convert_file(self):
		result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' })
		assert result.save_files(tempfile.gettempdir())
		assert result.conversion_cost > 0

	def test_convert_file_no_parallelizm(self):
		convertapi.max_parallel_uploads = 1
		result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' })
		assert result.save_files(tempfile.gettempdir())

	def test_convert_file_alternative(self):
		result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx', 'Converter': 'openoffice' })
		assert result.save_files(tempfile.gettempdir())
		assert result.conversion_cost > 0

	def test_convert_file_url(self):
		result = convertapi.convert('pdf', { 'File': 'https://cdn.convertapi.com/cara/testfiles/document.docx?test=1' })
		assert result.conversion_cost > 0

	def test_convert_url(self):
		result = convertapi.convert('pdf', { 'Url': 'http://convertapi.com' })
		assert result.conversion_cost > 0

	def test_convert_url_with_timeout_and_format(self):
		result = convertapi.convert('pdf', { 'Url': 'https://www.w3.org/TR/PNG/iso_8859-1.txt' }, 'web', 100)
		assert result.conversion_cost > 0

	def test_upload_io(self):
		bytes_io = io.BytesIO(b'test')
		upload_io = convertapi.UploadIO(bytes_io, 'test.txt')
		result = convertapi.convert('pdf', { 'File': upload_io })
		assert result.conversion_cost > 0

	def test_download_io(self):
		result = convertapi.convert('pdf', { 'Url': 'https://www.w3.org/TR/PNG/iso_8859-1.txt' })
		assert len(result.file.io.getvalue()) > 0

	def test_zip_files(self):
		files = ['examples/files/test.docx', 'examples/files/test.docx']
		result = convertapi.convert('zip', { 'Files': files })
		assert result.conversion_cost > 0

	def test_chained_conversion(self):
		result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' })
		zip_result = convertapi.convert('zip', { 'Files': result.files })
		eq_('test.zip', zip_result.file.filename)

	def test_compare_files(self):
		file = 'examples/files/test.docx'
		result = convertapi.convert('compare', { 'File': file, 'CompareFile': file })
		assert result.conversion_cost > 0

	@raises(convertapi.ApiError)
	def test_api_error(self):
		convertapi.api_secret = 'TEST'
		convertapi.convert('pdf', { 'Url': 'https://www.w3.org/TR/PNG/iso_8859-1.txt' })

	def test_user_info(self):
		user_info = convertapi.user()
		assert user_info['Active']

	@responses.activate
	def test_with_token(self):
		convertapi.api_token = 'TEST'
		responses.add(responses.POST, 'https://v2.convertapi.com/convert/web/to/pdf?Token=TEST', json = { 'ConversionCost': 123 })
		result = convertapi.convert('pdf', { 'Url': 'dummyurl' })
		assert result.conversion_cost == 123

	@responses.activate
	def test_with_token_and_api_key(self):
		convertapi.api_token = 'TEST'
		convertapi.api_key = 1
		responses.add(responses.POST, 'https://v2.convertapi.com/convert/web/to/pdf?Token=TEST&ApiKey=1', json = { 'ConversionCost': 123 })
		result = convertapi.convert('pdf', { 'Url': 'dummyurl' })
		assert result.conversion_cost == 123
