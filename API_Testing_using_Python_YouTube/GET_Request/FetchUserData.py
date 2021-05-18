"""
This file contains logic on getting user data from an API
"""

######################################################################################################################
# ########################################### Video 1 Code and Notes ############################################### #
######################################################################################################################

# # Imports
# import requests
#
# # Api URL - GET Request
# url = 'https://reqres.in/api/users?page=2'
#
# # Send a get request
# response = requests.get(url)
#
# # Display the Response Code
# print(f'Response Code: {response}')
#
# # Display Response content
# print(f'Response Content: {response.content}')
#
# # Display the Response header
# print(f'Response Header: {response.headers}')

######################################################################################################################
# ########################################### Video 2 Code and Notes ############################################### #
######################################################################################################################

# Imports
import requests
import json
import jsonpath

# Api URL - GET Request
url = 'https://reqres.in/api/users?page=2'

# Send a get request
response = requests.get(url)

# Display Response content
print(f'Response Content: {response.content}')

# Parse response to JSON format
json_resp = json.loads(response.text)

# Display in the JSON format
print(f'Response Content in JSON Format: {json_resp}')

# Fetch specific value using JSON path
# This will return a list
pages = jsonpath.jsonpath(json_resp, 'total_pages')

# Display pages
print(f'Number of pages: {pages[0]}')

# Verify that the number of pages is what is expected
# If True it will just finish with exit code 0, meaning successful,
#   if False, will throw an AssertionError message
assert pages[0] == 2


