__version__ = '0.0.1'

from .exceptions import *
from .configuration import Configuration
from .client import Client

configuration = Configuration()
client = Client(configuration)
