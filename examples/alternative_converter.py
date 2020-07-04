import convertapi
import os
import tempfile

convertapi.api_secret = os.environ['CONVERT_API_SECRET'] # your api secret

# Example of saving Word docx to PDF using OpenOffice converter
# https://www.convertapi.com/doc-to-pdf/openoffice

upload_io = convertapi.UploadIO(open('files/test.docx', 'rb'))
params = { 'File': upload_io, 'converter': 'openoffice' }

saved_files = convertapi.convert('pdf', params).save_files(tempfile.gettempdir())

print("The PDF saved to %s" % saved_files)
