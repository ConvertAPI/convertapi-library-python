__version__ = '2.0.0'

from .exceptions import *
from .client import Client
from .upload_io import UploadIO
from .api import convert, user

# configuration

api_credentials = None
base_uri = 'https://v2.convertapi.com/'
user_agent = 'ConvertAPI-Python/' + __version__
timeout = 1800
conversion_timeout = None
conversion_timeout_delta = 10
upload_timeout = None
download_timeout = None
max_parallel_uploads = 10
verify_ssl = True

client = Client()
