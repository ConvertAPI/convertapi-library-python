import convertapi
import os
import tempfile

convertapi.api_credentials = os.environ['CONVERT_API_SECRET'] # your api secret or token

# Example of converting Web Page URL to PDF file
# https://www.convertapi.com/web-to-pdf

result = convertapi.convert(
    'pdf',
    {
        'Url': 'https://en.wikipedia.org/wiki/Data_conversion',
        'FileName': 'web-example',
    },
    from_format = 'web',
    timeout = 180,
)

saved_files = result.save_files(tempfile.gettempdir())

print("The web page PDF saved to %s" % saved_files)
