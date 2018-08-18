import os

from .result_file import ResultFile
from .upload_io import UploadIO

def build(resource):
    if isinstance(resource, ResultFile):
        return resource.url

    if isinstance(resource, UploadIO):
        return resource.upload()

    if os.path.isfile(resource):
        io = open(resource, 'rb')
        return UploadIO(io).upload()

    return resource
