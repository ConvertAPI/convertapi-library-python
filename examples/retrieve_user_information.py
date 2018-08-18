import convertapi
import os

convertapi.api_secret = os.environ['CONVERT_API_SECRET'] # your api secret

# Retrieve user information
# https://www.convertapi.com/doc/user

print(convertapi.user())
