"""
This file contains logic for creating and testing a delete request.
"""

######################################################################################################################
# ########################################### Video 3 Code and Notes ############################################### #
######################################################################################################################

# Imports
import requests

# Api URL - DELETE Request
url = 'https://reqres.in/api/users/2'

# Send the delete request
response = requests.delete(url)

# Get the response code
print(f'Response Status Code: {response.status_code}')

# To verify that we are getting the proper status code
assert response.status_code == 204
