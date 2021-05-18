# API Testing using Python - Write Test Case - PUT Request

[Video Link](https://youtu.be/OdFW3RwAz8w)

## Description: 
 - NOTE: This description was taken from the video description.

**✪✪✪ API Testing using Python - Write First Test Case - Get Request ✪✪✪**

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖  

In Python, we use requests library for REST API Testing  

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

- A "PUT" request is used for updating a resource on the server.

- Notes are in the `Update.py` file under the divider for "Video 5 Code and Notes"

- First have to import `requests`, `json`, and `jsonpath`

- Need the API url for the Put Request

- Create a `json` file with the data you want to add to the server in the proper format based on the API instructions.

- Open, read in, and parse the json file into the proper format:

    ```
    # Open the json file - need to use .. in front of / because I am going 
    #   one directory up from the current directory
    file = open('../UpdateUser.json', 'r')
    
    # Read in the json file - returns a string
    json_in = file.read()
    
    # Load the json file - parses the string into json format
    request_json = json.loads(json_in)
    ```

- Send the "PUT" request to the API: `response = requests.put(url, request_json)`

    - The first parameter is the url from the API
    
    - The second parameter is the request body (in this case, the parsed json file)

- According to the API we should be getting a `200` status code, to check that we are getting the right status code: `print(response.status_code)`

- Then can also verify the correct status code using the assert method: `assert response.status_code == 200`.

- More notes and code can be found in the `Update.py` file.
