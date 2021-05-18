# API Testing using Python - Write Test Case - in Pytest Format

[Video Link](https://youtu.be/wWVXf1WWCl0)

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

- Create a new directory `TestCases`

- Create a new file `test_CreateNew.py` in the `TestCases` directory.

- Copy and paste the code from the `CreateNew.py` file into the `Test_CreateNew.py` file.

- Define a function for testing the code:

  ```
  def test_create_new():
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
  ```
  
- In the terminal, run `pytest TestCases` and it will automatically know that the files in there are all test files because they start with `test_` and the functions also start with `test_`

- You can also add multiple test cases in the same file as long as they have different names for the function and start with `test_`.

- You can also run the command as: `pytest -v TestCases` to get details of the testing. This is great to use if you are running multiple tests at once because it will show you which test passed and which failed, if any. The `-v` stands for `verbose`.

- You can also run a single test file with the follow command, when you are in the testing directory: `pytest <test_filename.py>`.
