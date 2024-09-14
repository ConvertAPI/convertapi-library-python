import convertapi
import os
import tempfile

convertapi.api_credentials = os.environ['CONVERT_API_SECRET'] # your api secret or token

# Short example of conversions chaining, the PDF pages extracted and saved as separated JPGs and then ZIP'ed
# https://www.convertapi.com/doc/chaining

print('Converting PDF to JPG and compressing result files with ZIP')

jpg_result = convertapi.convert('jpg', { 'File': 'files/test.pdf' })

print("Conversions done. Cost: %s. Total files created: %s" % (jpg_result.conversion_cost, len(jpg_result.files)))

zip_result = convertapi.convert('zip', { 'Files': jpg_result.files })

print("Conversions done. Cost: %s. Total files created: %s" % (zip_result.conversion_cost, len(zip_result.files)))

saved_files = zip_result.save_files(tempfile.gettempdir())

print("File saved to %s" % saved_files)
