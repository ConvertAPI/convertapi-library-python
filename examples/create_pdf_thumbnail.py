import convertapi
import os
import tempfile

convertapi.api_secret = os.environ['CONVERT_API_SECRET'] # your api secret

# Example of extracting first page from PDF and then chaining conversion PDF page to JPG.
# https://www.convertapi.com/pdf-to-extract
# https://www.convertapi.com/pdf-to-jpg

pdf_result = convertapi.convert(
    'extract',
    {
        'File': 'files/test.pdf',
        'PageRange': 1,
    }
)

jpg_result = convertapi.convert(
    'jpg',
    {
        'File': pdf_result,
        'ScaleImage': True,
        'ScaleProportions': True,
        'ImageHeight': 300,
        'ImageWidth': 300,
    }
)

saved_files = jpg_result.save_files(tempfile.gettempdir())

print("The thumbnail saved to %s" % saved_files)
