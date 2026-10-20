import os

import pytest

import convertapi


@pytest.fixture(autouse=True)
def configuration():
	"""Give every test the default configuration and restore it afterwards."""
	saved = {name: getattr(convertapi, name) for name in ('api_credentials', 'base_uri', 'max_parallel_uploads')}
	yield
	for name, value in saved.items():
		setattr(convertapi, name, value)


@pytest.fixture
def live():
	"""Credentials for tests that call the real service.

	CONVERT_API_SECRET is the API token. CONVERT_API_BASE_URI optionally points the tests at another
	deployment (e.g. https://stag-v2.convertapi.com/); it defaults to the library's own base_uri.
	"""
	secret = os.environ.get('CONVERT_API_SECRET')
	if not secret:
		pytest.skip('CONVERT_API_SECRET is not set')
	convertapi.api_credentials = secret
	convertapi.base_uri = os.environ.get('CONVERT_API_BASE_URI') or convertapi.base_uri
