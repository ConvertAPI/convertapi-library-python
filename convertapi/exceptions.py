class ConvertApiError(BaseException):
	def __init__(self, *args, **kwargs):
		super(ConvertApiError, self).__init__(*args, **kwargs)
