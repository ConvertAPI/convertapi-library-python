# ConvertAPI Python Client

[![PyPI version](https://badge.fury.io/py/convertapi.svg)](https://badge.fury.io/py/convertapi)
[![Build Status](https://secure.travis-ci.org/ConvertAPI/convertapi-python.svg)](http://travis-ci.org/ConvertAPI/convertapi-python)

## Convert your files with our online file conversion API

The ConvertAPI helps converting various file formats. Creating PDF and Images from various sources like Word, Excel, Powerpoint, images, web pages or raw HTML codes. Merge, Encrypt, Split, Repair and Decrypt PDF files. And many others files manipulations. In just few minutes you can integrate it into your application and use it easily.

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

### File conversion

Example to convert file to PDF. All supported formats and options can be found
[here](https://www.convertapi.com).

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

ConvertAPI accepts extra conversion parameters depending on converted formats. All conversion
parameters and explanations can be found [here](https://www.convertapi.com).

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

You can always check remaining seconds amount by fetching [user information](https://www.convertapi.com/doc/user).

```python
user_info = convertapi.user()

print(user_info['SecondsLeft'])
```

### More examples

You can find more advanced examples in the [/examples](https://github.com/ConvertAPI/convertapi-python/tree/master/examples) folder.

## Development

Execute `CONVERT_API_SECRET=your_secret nosetests --nocapture` to run the tests.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/ConvertAPI/convertapi-python. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
