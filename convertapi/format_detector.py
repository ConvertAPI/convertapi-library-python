from os.path import splitext
from io import FileIO
from requests import utils
from .result import Result
from .upload_io import UploadIO

def detect(resource):
    if isinstance(resource, UploadIO):
        return resource.file_ext
    elif 'filename' in dir(resource):
        path = resource.filename
    elif isinstance(resource, FileIO):
        path = resource.name
    elif isinstance(resource, Result):
        path = resource.file.filename
    else:
        path = utils.urlparse(resource).path

    return splitext(path)[1][1:].lower()
