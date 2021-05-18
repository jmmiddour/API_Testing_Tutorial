"""
This file contains ...
"""

# Imports
import requests
import json
import jsonpath


def test_add_new_data():
    # Add the api url for the student details
    app_url = "http://thetestingworldapi.com/api/studentsDetails"

    # Open the json file, have to have it ././ for the testing file
    f = open('././NewStudent.json', 'r')
    # f = open('../NewStudent.json', 'r')  # Use if running file directly

    # Parse the json file into a json format
    request_json = json.loads(f.read())

    # Create the post request
    response = requests.post(app_url, request_json)

    # Get the student id assigned when created to use later
    stud_id = jsonpath.jsonpath(response.json(), 'id')

    # Display the response text
    print(f'New Student Response Text: {response.text}\n')

    # Get the id to use later
    resp_id = jsonpath.jsonpath(response.json(), 'id')

    # Display the id number
    print(f'New Student Response ID number: {resp_id}\n')

    """
    Add new Technical Skills
    """
    # Add the api url for the technical skills
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"

    # Open the json file, have to have it ././ for the testing file
    f = open('././NewTech.json', 'r')

    # Parse the json file into a json format
    request_json = json.loads(f.read())

    # Assign the id given when creating new student to the id field in the json file
    request_json['id'] = int(stud_id[0])

    # Assign the id given when creating new student to the st_id field in the json file
    request_json['st_id'] = stud_id[0]

    # Create the post request
    response = requests.post(tech_api_url, request_json)

    # Display the response text
    print(f'New Skills Response Text: {response.text}\n')

    """
    Add new address
    """
    # Add the api url for the addresses
    address_api_url = "http://thetestingworldapi.com/api/addresses"

    # Open the json file, have to have it ././ for the testing file
    f = open('././NewAddress.json', 'r')

    # Parse the json file into a json format
    request_json = json.loads(f.read())

    # Assign the id given when creating new student to the stId field in the json file
    request_json['stId'] = stud_id[0]

    # Create the post request
    response = requests.post(address_api_url, request_json)

    # Display the response text
    print(f'New Address Response Text: {response.text}\n')

    """
    Get the final details
    """
    # Add the api url for the final student details
    details_api_url = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(stud_id[0])

    # Create the get request
    response = requests.get(details_api_url)

    # Display the response text
    print(f'Details Response Text: {response.text}')


# # Use this to display the print statements in the function.
# if __name__ == '__main__':
#     test_add_new_data()
