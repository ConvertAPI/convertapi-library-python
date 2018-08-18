import convertapi
import os.path

class UploadIO:
    def __init__(self, io, filename = None):
        self.io = io
        self._filename = filename
        self._file_id = None

    @property
    def file_id(self):
        if self._file_id is None:
            self._file_id = self.__upload()

        return self._file_id

    @property
    def filename(self):
        if self._filename:
            return self._filename

        if 'name' in dir(self.io):
            return os.path.basename(self.io.name)

        raise 'Filename must be provided for non File resources'

    def __upload(self):
        result = convertapi.client.upload(self.io, self.filename)
        return result['FileId']
