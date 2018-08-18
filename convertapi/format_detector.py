from os.path import splitext
from io import FileIO
from requests import utils

def detect(resource):
    if 'filename' in dir(resource):
        path = resource.filename
    elif isinstance(resource, FileIO):
        path = resource.name
    else:
        path = utils.urlparse(resource).path

    return splitext(path)[1][1:].lower()