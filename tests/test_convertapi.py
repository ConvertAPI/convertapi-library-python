import io
import tempfile

import pytest

import convertapi

pytestmark = [pytest.mark.live, pytest.mark.usefixtures('live')]


def test_convert_file():
	result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' })
	assert result.save_files(tempfile.gettempdir())
	assert result.conversion_cost > 0

def test_convert_file_no_parallelizm():
	convertapi.max_parallel_uploads = 1
	result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' })
	assert result.save_files(tempfile.gettempdir())

def test_convert_file_url():
	result = convertapi.convert('pdf', { 'File': 'https://cdn.convertapi.com/cara/testfiles/document.docx?test=1' })
	assert result.conversion_cost > 0

def test_convert_url():
	result = convertapi.convert('pdf', { 'Url': 'http://convertapi.com' })
	assert result.conversion_cost > 0

def test_convert_url_with_timeout_and_format():
	result = convertapi.convert('pdf', { 'Url': 'https://www.w3.org/TR/PNG/iso_8859-1.txt' }, 'web', 100)
	assert result.conversion_cost > 0

def test_upload_io():
	bytes_io = io.BytesIO(b'test')
	upload_io = convertapi.UploadIO(bytes_io, 'test.txt')
	result = convertapi.convert('pdf', { 'File': upload_io })
	assert result.conversion_cost > 0

def test_download_io():
	result = convertapi.convert('pdf', { 'Url': 'https://www.w3.org/TR/PNG/iso_8859-1.txt' })
	assert len(result.file.io.getvalue()) > 0

def test_zip_files():
	files = ['examples/files/test.docx', 'examples/files/test.docx']
	result = convertapi.convert('zip', { 'Files': files })
	assert result.conversion_cost > 0

def test_chained_conversion():
	result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' })
	zip_result = convertapi.convert('zip', { 'Files': result.files })
	assert zip_result.file.filename == 'test.zip'

def test_compare_files():
	file = 'examples/files/test.docx'
	result = convertapi.convert('compare', { 'File': file, 'CompareFile': file })
	assert result.conversion_cost > 0

def test_api_error():
	convertapi.api_credentials = 'TEST'
	with pytest.raises(convertapi.ApiError):
		convertapi.convert('pdf', { 'Url': 'https://www.w3.org/TR/PNG/iso_8859-1.txt' })

def test_user_info():
	user_info = convertapi.user()
	assert user_info['Active']
