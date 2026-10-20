"""Tests that need no network: the ConvertAPI service is mocked with `responses`."""

import io
import json
from urllib.parse import parse_qs

import pytest
import responses

import convertapi

BASE = 'https://v2.convertapi.com/'


@pytest.fixture(autouse=True)
def credentials():
	convertapi.api_credentials = 'test-token'


def conversion(*files):
	return {
		'ConversionCost': 1,
		'Files': [{ 'FileName': name, 'FileSize': 4, 'Url': 'https://v2.convertapi.com/d/' + name } for name in files],
	}


def form(call):
	return { k: v[0] for k, v in parse_qs(call.request.body).items() }


def test_defaults():
	assert convertapi.base_uri == BASE
	assert convertapi.user_agent == 'ConvertAPI-Python/' + convertapi.__version__


def test_configuration():
	convertapi.api_credentials = 'TEST'
	assert convertapi.api_credentials == 'TEST'


@responses.activate
def test_user_sends_token_and_user_agent():
	responses.get(BASE + 'user', json={ 'Active': True })

	assert convertapi.user()['Active']

	headers = responses.calls[0].request.headers
	assert headers['Authorization'] == 'Bearer test-token'
	assert headers['User-Agent'] == convertapi.user_agent


@responses.activate
def test_convert_url():
	responses.post(BASE + 'convert/web/to/pdf', json=conversion('page.pdf'))

	result = convertapi.convert('pdf', { 'Url': 'https://example.com' })

	assert result.conversion_cost == 1
	assert result.file.filename == 'page.pdf'
	assert form(responses.calls[0]) == { 'Url': 'https://example.com', 'StoreFile': 'True' }


@responses.activate
def test_convert_with_format_and_timeout():
	responses.post(BASE + 'convert/web/to/pdf', json=conversion('page.pdf'))

	convertapi.convert('pdf', { 'Url': 'https://example.com/a.txt' }, 'web', 100)

	assert form(responses.calls[0])['Timeout'] == '100'
	assert responses.calls[0].request.req_kwargs['timeout'] == 100 + convertapi.conversion_timeout_delta


@responses.activate
def test_convert_file_uploads_it_first(tmp_path):
	responses.post(BASE + 'upload', json={ 'FileId': 'abc', 'FileExt': 'docx' })
	responses.post(BASE + 'convert/docx/to/pdf', json=conversion('test.pdf'))
	responses.get('https://v2.convertapi.com/d/test.pdf', body=b'%PDF')

	result = convertapi.convert('pdf', { 'File': 'examples/files/test.docx' })
	saved = result.save_files(str(tmp_path))

	upload = responses.calls[0].request
	assert upload.headers['Content-Disposition'] == "attachment; filename*=UTF-8''test.docx"
	assert form(responses.calls[1])['File'] == 'abc'
	assert saved == [str(tmp_path / 'test.pdf')]
	assert (tmp_path / 'test.pdf').read_bytes() == b'%PDF'


@responses.activate
def test_upload_io_and_download_io():
	responses.post(BASE + 'upload', json={ 'FileId': 'abc', 'FileExt': 'txt' })
	responses.post(BASE + 'convert/txt/to/pdf', json=conversion('test.pdf'))
	responses.get('https://v2.convertapi.com/d/test.pdf', body=b'%PDF')

	upload_io = convertapi.UploadIO(io.BytesIO(b'test'), 'test.txt')
	result = convertapi.convert('pdf', { 'File': upload_io })

	assert result.file.io.getvalue() == b'%PDF'
	assert responses.calls[0].request.body == b'test'


@responses.activate
def test_chained_conversion_passes_result_urls():
	responses.post(BASE + 'convert/any/to/zip', json=conversion('test.zip'))
	previous = convertapi.result.Result(conversion('a.pdf', 'b.pdf'))

	convertapi.convert('zip', { 'Files': previous.files })

	sent = form(responses.calls[0])
	assert sent['Files[0]'] == 'https://v2.convertapi.com/d/a.pdf'
	assert sent['Files[1]'] == 'https://v2.convertapi.com/d/b.pdf'


@responses.activate
def test_api_error():
	responses.post(BASE + 'convert/web/to/pdf', status=401, json={ 'Code': 4011, 'Message': 'Unauthorized.' })

	with pytest.raises(convertapi.ApiError) as error:
		convertapi.convert('pdf', { 'Url': 'https://example.com' })

	assert error.value.code == 4011
	assert str(error.value) == 'Unauthorized. Code: 4011.'


@responses.activate
def test_http_error_without_json_body():
	responses.post(BASE + 'convert/web/to/pdf', status=502, body='Bad Gateway')

	with pytest.raises(Exception) as error:
		convertapi.convert('pdf', { 'Url': 'https://example.com' })

	assert '502' in str(error.value)
