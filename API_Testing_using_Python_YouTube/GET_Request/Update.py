"""
This file contains logic for creating and testing a Put request.
"""

######################################################################################################################
# ########################################### Video 5 Code and Notes ############################################### #
######################################################################################################################

# Imports
import requests
import json
import jsonpath

# Api URL - PUT Request
url = 'https://reqres.in/api/users/2'

# Open the json file - need to use .. in front of / because I am going
#   one directory up from the current directory
file = open('../UpdateUser.json', 'r')

# Read in the json file - returns a string
json_in = file.read()

# Load the json file - parses the string into json format
request_json = json.loads(json_in)

# Display the json file to verify it is loaded in properly
print(f'JSON File Imported: {request_json}')

# Send the Post request with json input as the response body
response = requests.put(url, request_json)

# Display the content of the response
print(f'Response Content: {response.content}')

# Verify the proper response code is returned
assert response.status_code == 200

# Parse response to json format
response_json = json.loads(response.text)

# Get the updatedAt from the response
resp_update = jsonpath.jsonpath(response_json, 'updatedAt')

# Display when it was updated at
print(f'"Updated At" from JSON Response: {resp_update[0]}')
