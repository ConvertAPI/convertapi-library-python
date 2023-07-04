# ConvertAPI Python Client

[![PyPI version](https://badge.fury.io/py/convertapi.svg)](https://badge.fury.io/py/convertapi)
[![Build Status](https://github.com/ConvertAPI/convertapi-python/actions/workflows/main.yml/badge.svg)](https://github.com/ConvertAPI/convertapi-python/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Convert your files with our online file conversion API

ConvertAPI helps to convert various file formats. Creating PDF and Images from various sources like Word, Excel, Powerpoint, images, web pages or raw HTML codes. Merge, Encrypt, Split, Repair and Decrypt PDF files and many other manipulations. You can integrate it into your application in just a few minutes and use it easily.

## Installation

Install with [pip](https://pypi.org/project/pip/):

    pip install --upgrade convertapi

Install from source with:

    python setup.py install

### Requirements

* Python 2.7+ or Python 3.3+

## Usage

### Configuration

You can get your secret at https://www.convertapi.com/a

```python
import convertapi

convertapi.api_secret = 'your-api-secret'
```

#### Proxy configuration

If you need to use a proxy, you can specify it using `HTTPS_PROXY` environment variable when running your script.

Example:

```
CONVERT_API_SECRET=secret HTTPS_PROXY=https://user:pass@127.0.0.1:9000/ python convert_word_to_pdf_and_png.py
```

### File conversion

Convert a file to PDF example. All supported file formats and options can be found
[here](https://www.convertapi.com/conversions).

```python
result = convertapi.convert('pdf', { 'File': '/path/to/my_file.docx' })

# save to file
result.file.save('/path/to/save/file.pdf')
```

Other result operations:

```python
# save all result files to folder
result.save_files('/path/to/save/files')

# get conversion cost
conversion_cost = result.conversion_cost
```

#### Convert file url

```python
result = convertapi.convert('pdf', { 'File': 'https://website/my_file.docx' })
```

#### Specifying from format

```python
result = convertapi.convert(
    'pdf',
    { 'File': '/path/to/my_file' },
    from_format = 'docx'
)
```

#### Additional conversion parameters

ConvertAPI accepts additional conversion parameters depending on selected formats. All conversion
parameters and explanations can be found [here](https://www.convertapi.com/conversions).

```python
result = convertapi.convert(
    'pdf',
    {
        'File': '/path/to/my_file.docx',
        'PageRange': '1-10',
        'PdfResolution': '150',
    }
)
```

### User information

You can always check your remaining seconds amount programatically by fetching [user information](https://www.convertapi.com/doc/user).

```python
user_info = convertapi.user()

print(user_info['SecondsLeft'])
```

### Alternative domain

Set `base_uri` parameter to use other service domains. Dedicated to the region [domain list](https://www.convertapi.com/doc/servers-location).

```
convertapi.base_uri = 'https://eu-v2.convertapi.com/'
```

### More examples

Find more advanced examples in the [/examples](https://github.com/ConvertAPI/convertapi-python/tree/master/examples) folder.

## Development

Execute `CONVERT_API_SECRET=your_secret nosetests --nocapture` to run the tests.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/ConvertAPI/convertapi-python. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
