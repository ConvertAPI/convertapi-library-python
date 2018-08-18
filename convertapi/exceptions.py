class BaseError(BaseException):
	pass

class ApiError(BaseError):
	def __init__(self, result):
		super(ApiError, self).__init__(result['Message'])

		self.code = result['Code']
		self.invalid_parameters = result['InvalidParameters']

	def __str__(self):
 		return  "%s Code: %s. %s" % (self.message, self.code, self.invalid_parameters)
