import convertapi
import os
import tempfile

convertapi.api_credentials = os.environ['API_TOKEN'] # your api token

# Example of converting Web Page URL to PDF file
# https://www.convertapi.com/html-to-pdf

result = convertapi.convert(
    'pdf',
    {
        'Url': 'https://cdn.convertapi.com/public/files/demo',
        'FileName': 'web-example',
    },
    from_format = 'html',
    timeout = 180,
)

saved_files = result.save_files(tempfile.gettempdir())

print("The web page PDF saved to %s" % saved_files)
