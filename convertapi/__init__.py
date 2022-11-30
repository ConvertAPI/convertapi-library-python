__version__ = '1.5.0'

from .exceptions import *
from .client import Client
from .upload_io import UploadIO
from .api import convert, user, async_convert, async_poll

# configuration

api_secret = None
base_uri = 'https://v2.convertapi.com/'
user_agent = 'ConvertAPI-Python/' + __version__
timeout = 1800
conversion_timeout = None
conversion_timeout_delta = 10
upload_timeout = 1800
download_timeout = 1800
max_parallel_uploads = 10

client = Client()
