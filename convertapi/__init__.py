__version__ = '1.1.1'

from .exceptions import *
from .client import Client
from .upload_io import UploadIO
from .api import convert, user

# configuration

api_secret = None
base_uri = 'https://v2.convertapi.com/'
user_agent = 'ConvertAPI-Python/' + __version__
timeout = 60
conversion_timeout = 180
conversion_timeout_delta = 10
upload_timeout = 600
download_timeout = 600
max_parallel_uploads = 10

client = Client()
