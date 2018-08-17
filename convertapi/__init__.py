__version__ = '0.0.1'

from .exceptions import *
from .configuration import Configuration
from .client import Client
from .api import convert

configuration = Configuration()
client = Client(configuration)
