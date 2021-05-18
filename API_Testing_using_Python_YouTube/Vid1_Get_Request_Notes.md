# API Testing using Python - Write First Test Case - Get Request

[Video Link](https://youtu.be/3ts5fzmhN5o)

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

- Need to have the following packages installed:
  
    - `Requests` - `pip install requests`
      
        - If your package is an older version `pip install -U requests`
        
    - `Json` - already built in to Python, no need for installing.
      
    - `Jsonpath` - `pip install jsonpath`
      
        - Same as request, if your package is an older version install updated version.
    
- Could also install the above via a requirements file and install them into a virtual environment, 
  which is the better way to go.
  
    - Create a file `requirements.txt` and add the 2 above packages.
    
    - In the command line:
    
        - `python -m venv <name of environment>` - creates a new folder in the current directory 
          with all the environmental variables for this project.
          
        - `source <name of environment>/Scripts/activate` when using the bash command line tool on a Windows machine.
    
        - `pip install -r requirements.txt` to install the packages listed in the requirements file.
    
    - Then, if using PyCharm, ensure that you configure your python interpreter to the new virtual environment.
    
- Create a new directory, `GET_Request`

- Inside the `GET_Request` directory, create a file, `FetchUserData.py`

- Further notes are in the `FetchUserData.py` file.
