import convertapi
import os
import tempfile

convertapi.api_secret = os.environ['CONVERT_API_SECRET'] # your api secret

# Example of extracting first and last pages from PDF and then merging them back to new PDF.
# https://www.convertapi.com/pdf-to-split
# https://www.convertapi.com/pdf-to-merge

split_result = convertapi.convert('split', { 'File': 'files/test.pdf' })

first_page = split_result.files[0]
last_page = split_result.files[-1]
files = [first_page, last_page]

merge_result = convertapi.convert('merge', { 'Files': files })

saved_files = merge_result.save_files(tempfile.gettempdir())

print("The PDF saved to %s" % saved_files)
