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

    @property
    def io(self):
        if not hasattr(self, '_io'):
            self._io = convertapi.client.download_io(self.url)

        return self._io

    def save(self, path):
        if os.path.isdir(path):
            path = os.path.join(path, self.filename)

        return convertapi.client.download(self.url, path)
