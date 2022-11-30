import convertapi

from convertapi import file_param, format_detector, utils
from .result import Result

DEFAULT_URL_FORMAT = 'web'

class Task:
    def __init__(self, from_format, to_format, params, timeout = None, is_async = False):
        self.from_format = from_format
        self.to_format = to_format
        self.params = params
        self.timeout = timeout or convertapi.conversion_timeout
        self.is_async = is_async

        self.default_params = {
            'Timeout': self.timeout,
            'StoreFile': True,
        }

    def run(self):
        params = self.__normalize_params()
        from_format = self.from_format or self.__detect_format()
        timeout = self.timeout + convertapi.conversion_timeout_delta if self.timeout else None
        base_path = 'convert' if not self.is_async else 'async/convert'
        path = "%s/%s/to/%s" % (base_path, from_format, self.to_format)

        if 'converter' in params:
            path += "/converter/%s" % (params['converter'])

        response = convertapi.client.post(path, params, timeout = timeout)

        return Result(response)

    def __normalize_params(self):
        params = {}

        for k, v in self.params.items():
            if k == 'File':
                params[k] = file_param.build(v)
            elif k == 'Files':
                results = utils.map_in_parallel(file_param.build, v, convertapi.max_parallel_uploads)

                for idx, val in enumerate(results):
                    key = '%s[%i]' % (k, idx)
                    params[key] = val
            else:
                params[k] = v

        params.update(self.default_params)

        return params

    def __detect_format(self):
        if str(self.to_format).lower() == 'zip':
            return 'any'

        if 'Url' in self.params:
            return DEFAULT_URL_FORMAT

        if 'File' in self.params:
            return format_detector.detect(self.params['File'])

        if 'Files' in self.params:
            return format_detector.detect(self.params['Files'][0])
