import convertapi
import os.path

class UploadIO:
    def __init__(self, io, filename = None):
        self.io = io
        self.__filename = filename

    def upload(self):
        result = convertapi.client.upload(self.io, self.filename)
        return result['FileId']

    @property
    def filename(self):
        if self.__filename:
            return self.__filename

        if 'name' in dir(self.io):
            return os.path.basename(self.io.name)

        raise 'Filename must be provided for non File resources'
