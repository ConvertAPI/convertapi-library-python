import os
import convertapi

from .result_file import ResultFile

def build(resource):
    if isinstance(resource, ResultFile):
        return resource.url

    if os.path.isfile(resource):
        return __upload_file(resource)

    return resource

def __upload_file(file):
    filename = os.path.basename(file)

    with open(file, 'rb') as f:
        result = convertapi.client.upload(f, filename)
        return result['FileId']
