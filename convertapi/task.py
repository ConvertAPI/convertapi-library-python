import convertapi

from .result import Result

class Task:
    def __init__(self, from_format, to_format, params, conversion_timeout = None):
        self.from_format = from_format
        self.to_format = to_format
        self.params = params
        self.conversion_timeout = conversion_timeout or convertapi.conversion_timeout

        self.default_params = {
            'Timeout': self.conversion_timeout,
            'StoreFile': True,
        }

    def run(self):
        params = self.__normalize_params()
        from_format = self.from_format
        timeout = self.conversion_timeout + convertapi.conversion_timeout_delta
        path = "convert/%s/to/%s" % (from_format, self.to_format)

        response = convertapi.client.post(path, params, timeout = timeout)

        return Result(response)

    def __normalize_params(self):
        params = self.params.copy()
        params.update(self.default_params)
        return params