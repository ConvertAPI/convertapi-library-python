import convertapi
import os

class ResultFile:
    def __init__(self, info):
        self.info = info

    @property
    def url(self):
        return self.info['Url']

    @property
    def filename(self):
        return self.info['FileName']

    @property
    def size(self):
        return self.info['FileSize']

    def save(self, path):
        if os.path.isdir(path):
            path = os.path.join(path, self.filename)

        return convertapi.client.download(self.url, path)
