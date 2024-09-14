import convertapi
import os

convertapi.api_credentials = os.environ['CONVERT_API_SECRET'] # your api secret or token

# Retrieve user information
# https://www.convertapi.com/doc/user

print(convertapi.user())
