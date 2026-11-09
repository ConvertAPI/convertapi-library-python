import convertapi
import os
import tempfile

convertapi.api_credentials = os.environ['API_TOKEN'] # your api token

# Example of converting the first page of a PDF to a JPG thumbnail.
# https://www.convertapi.com/pdf-to-jpg

jpg_result = convertapi.convert(
    'jpg',
    {
        'File': 'files/test.pdf',
        'PageRange': 1,
        'ImageHeight': 300,
        'ImageWidth': 300,
        'FitToSize': True,
    }
)

saved_files = jpg_result.save_files(tempfile.gettempdir())

print("The thumbnail saved to %s" % saved_files)
