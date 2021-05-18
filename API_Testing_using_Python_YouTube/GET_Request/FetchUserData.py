"""
This file contains logic on getting user data from an API
"""

# Imports
import requests

# Api URL - GET Request
url = 'https://reqres.in/api/users?page=2'

# Send a get request
response = requests.get(url)

# Display the Response Code
print(f'Response Code: {response}')

# Display Response content
print(f'Response Content: {response.content}')

# Display the Response header
print(f'Response Header: {response.headers}')
