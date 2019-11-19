class BaseError(BaseException):
	pass

class ApiError(BaseError):
	def __init__(self, result):
		self.message = result.get('Message', '[message not set]')

		super(ApiError, self).__init__(self.message)

		self.code = result.get('Code', '')
		self.invalid_parameters = result.get('InvalidParameters', '')

	def __str__(self):
		message = "%s Code: %s. %s" % (self.message, self.code, self.invalid_parameters)
		return message.strip()
