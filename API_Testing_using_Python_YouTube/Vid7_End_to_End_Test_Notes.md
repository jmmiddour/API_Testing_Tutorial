# API Testing using Python - Write End-to-End Test Case

[Video Link](https://youtu.be/itrgje2oqqU)

## Description: 
 - NOTE: This description was taken from the video description.

**✪✪✪ API Testing using Python - Write First Test Case - Get Request ✪✪✪**

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖  

In Python, we use requests library for REST API Testing  

Pytest: 
  - It's a unit testing framework for Python Programming  
  - We can use pytest for writing validation
  - We can add tags and control execution through it
  

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖  

**API Testing using Python video | How to Write First API Testing Test Case using Python programming with requests library**

**Pre-requisite:**

  - ✍Install Python
	
  - ✍Install Pycharm
	
  - ✍Install Robot Framework
	
  - ✍Create Project on Pycharm
	
  - ✍Create Python file

**REST API Testing Introduction using Python**

   - Write Python Code to send a Get Request
	 
   - Display Status Code coming in Response
	 
   - Display response body content
	 
   - Pick Response content using Python

**GET Request :  GET method (in REST API) is used to fetch data from the application**

- ✪ Install Request Module, Json and Json Path module
  
- ✪ Here we are going to make a GET Request of Rest API
  
- ✪ Whatever response we are going to fetch, Store that response in a variable 
  
- ✪ Display Complete Response
  
- ✪ Display Status Code

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖   

**✪✪✪ Robot Framework - API Testing ✪✪✪**

1. [Robot Framework - API Testing - Validate Response (Status code)](https://youtu.be/Mexu6NubeXQ) 
   
2. [Robot Framework - API Testing - Write Test case - POST request](https://youtu.be/nrY7usa22Xo) 
   
3. [Robot Framework - API Testing - Write Test case - DELETE request](https://youtu.be/8gf_MdBEwUM) 
   
4. [Robot Framework - API Testing - Write Test case - DELETE request](https://youtu.be/OyhlXJ_nlQk)

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

✪✪✪ [Check out the video playlist here](https://www.youtube.com/channel/UCsdoSHH5bucBf_wwtvWJfnQ/playlists) ✪✪✪

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

**Robot Framework – Python: All Video Course Links**

1. [Introduction to Robot Framework](https://youtu.be/cRgNs4H0OR0)
   
2. [Step by Step Installation](https://youtu.be/38HPxnrXMHo)
   
3. [Work on Textbox](https://youtu.be/7xCaZMrSsx8)
   
4. [Work on Button, Link, Radio Button and Checkbox](https://youtu.be/DBg0TZGTAkg)
   
5. [Write User defined keywords using Library Keywords](https://youtu.be/yYLfCbqxG1U)
   
6. [Write User defined keywords- Return Value (Resource Files)](https://youtu.be/i7IBt69Yk7o)
   
7. [Add Setup and Tear Down to Test Cases](https://youtu.be/2eF_hhOLGTQ)

3. [Robot Framework: Installation (Part 2)](https://youtu.be/NfzEZOXwA0M) 
   
4. [Robot Framework: Installation (Part 3)](https://youtu.be/uzfppzs6fpI)
   
5. [Robot Framework: First Test Case](https://youtu.be/cmwCi1TGPC4)

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

**API Testing using Postman: All Video Course Links**

1. [API Testing using Postman: What Is Postman](https://youtu.be/vlHPLTcWqJs)
   
2. [API Testing using Postman: Postman setup](https://youtu.be/3eUSBeljEmM)
   
3. [API Testing using Postman: Postman window walkthrough](https://youtu.be/1SEis_JDPoY)
   
4. [API Testing using Postman: End to End test case](https://youtu.be/qDb7v9MrQ38)
   
5. [API Testing using Postman: How to Write Code in POSTMAN](https://youtu.be/1FxKWHeAcDs)
   
6. [API Testing using Postman: Coding: Write Loop](https://youtu.be/C3JaeNQcs9o)

Thank you for watching the videos. Please subscribe to our channel Testing World!
Happy Learning!

---

## My Notes:

- Create a new file `test_end_to_end.py` in the `TestCases` directory.

- Create a new JSON file with the required parameters from the API, in this case `NewStudent.json`.

- Create a new JSON file with the required parameters from the API, in this case `NewTech.json`.

- Create a new JSON file with the required parameters from the API, in this case `NewAddress.json`.

- Define a function for testing the code:

  ```
  def test_end_to_end():
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
  ```
  
- In the terminal, run `pytest TestCases` and it will automatically know that the files in there are all test files because they start with `test_` and the functions also start with `test_`

- You can also add multiple test cases in the same file as long as they have different names for the function and start with `test_`.

- You can also run the command as: `pytest -v TestCases` to get details of the testing. This is great to use if you are running multiple tests at once because it will show you which test passed and which failed, if any. The `-v` stands for `verbose`.

- You can also run a single test file with the follow command, when you are in the testing directory: `pytest <test_filename.py>`.

- You can also use `-s` at the end of the pytest command to show the print statements in the test functions.
