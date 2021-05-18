"""
This file contains logic for creating and testing a Post request.
"""

######################################################################################################################
# ########################################### Video 4 Code and Notes ############################################### #
######################################################################################################################

# Imports
import requests
import json
import jsonpath

# Api URL - DELETE Request
url = 'https://reqres.in/api/users'

# Open the json file - need to use .. in front of / because I am going
#   one directory up from the current directory
file = open('../CreateUser.json', 'r')

# Read in the json file - returns a string
json_in = file.read()

# Load the json file - parses the string into json format
request_json = json.loads(json_in)

# Display the json file to verify it is loaded in properly
print(f'JSON File Imported: {request_json}')

# Send the Post request with json input as the response body
response = requests.post(url, request_json)

# Display the content of the response
print(f'Response Content: {response.content}')

# Verify the proper response code is returned
assert response.status_code == 201

# Get the full header data from the response
print(f'Full Response Header: {response.headers}')

# Get just the Content-Length from the header data from the response
print(f'Content Length from Header: {response.headers.get("Content-Length")}')

# Parse response to json format
response_json = json.loads(response.text)

# Get the id from the response
resp_id = jsonpath.jsonpath(response_json, 'id')

# Display the first id in the id list
print(f'Id from JSON Response: {resp_id[0]}')
