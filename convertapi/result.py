from .result_file import ResultFile

class Result:
    def __init__(self, response):
        self.response = response

    @property
    def conversion_cost(self):
        return self.response['ConversionCost']

    @property
    def file(self):
        return self.files[0]

    @property
    def files(self):
        return list(map(ResultFile, self.response['Files']))

    def save_files(self, path):
        return [file.save(path) for file in self.files]
