import convertapi
import os.path

class UploadIO:
    def __init__(self, io, filename = None):
        self.io = io
        self._filename = filename
        self._result = None

    @property
    def file_id(self):
        return self.__result['FileId']

    @property
    def file_ext(self):
        return self.__result['FileExt']

    @property
    def __result(self):
        if self._result is None:
            self._result = convertapi.client.upload(self.io, self.__build_filename())

        return self._result

    def __build_filename(self):
        if self._filename:
            return self._filename

        if 'name' in dir(self.io):
            return os.path.basename(self.io.name)

        raise 'Filename must be provided for non File resources'
