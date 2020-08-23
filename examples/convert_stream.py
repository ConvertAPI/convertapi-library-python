import convertapi
import os
import io
import tempfile

convertapi.api_secret = os.environ['CONVERT_API_SECRET'] # your api secret

# Example of using content stream to convert to pdf
# https://www.convertapi.com/txt-to-pdf

content = "Test content string"

upload_io = convertapi.UploadIO(content, 'test.txt')

result = convertapi.convert('pdf', { 'File': upload_io })

saved_files = result.save_files(tempfile.gettempdir())

print("The PDF saved to %s" % saved_files)

