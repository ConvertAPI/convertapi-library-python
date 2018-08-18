import os

from io import FileIO
from .result import Result
from .result_file import ResultFile
from .upload_io import UploadIO

def build(resource):
    if isinstance(resource, Result):
        return resource.file.url

    if isinstance(resource, ResultFile):
        return resource.url

    if isinstance(resource, UploadIO):
        return resource.file_id

    if isinstance(resource, FileIO):
        return UploadIO(resource).file_id

    if os.path.isfile(resource):
        io = open(resource, 'rb')
        return UploadIO(io).file_id

    return resource
