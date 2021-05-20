# Python Tutorial: Unit Testing Your Code with the unittest Module

### By [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)

[Link to YouTube Video](https://youtu.be/6tNS--WetLI)

## My Notes

### Why should we use `unittest` to test our code?

- When you write good tests for your code, it gives you more confidence that your updates and refactoring don't have any unintended consequences or break your code in any way. Like if you were to update a function in your project, those changes may have broken several sections of your code, even if that function itself is still working properly.

- Good `unittest` will ensure that everything is working and if it is not, it will show you exactly what is broken.

- `unittest` is a builtin module in Python, so no need to install any extra packages.

- Most people just use print statements in their code to test that it is working correctly. This way of testing is hard to automate and maintain. Plus if you are testing a lot of functions, it is difficult to find out what is failing and what succeeded at a glance.
    
### Testing `calc.py`

[Starts here in the video](https://youtu.be/6tNS--WetLI?t=121)

- Start by creating a test file, in this case we will start with `test_calc.py`:

    - Import `unittest` and the file you will be testing, in this case `calc`.
  
    - Create a test class that inherits from the `unittest.TestCase`.  This will give us access to a lot of testing capabilities within the class.
  
    - Then define your test(s). Always define the test method with a name that starts with `test_`. This is required, or it will not run that test method.
  
    - As with any class object, need to pass in self as an argument.
  
    - There are several `assert` methods that come with `TestCase` class and you can find them [here in the documentation for unittest](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug).
  
    - One that we will use in this case is `self.assertEqual(calc.add(10, 5), 15)`
  
        - param1: The first value: required
  
        - param2: The second value: required
  
        - param3: message: Optional
  
- In the command line, run `python -m unittest test_calc.py` to see the results of the test(s). If you just run `python test_calc.py` it will not return anything, unless you have the `if __name__ == '__main__'` block set up properly. Here you could just add to the body of that block `unittest.main()` and this will run all the test in this file.

- I was having a path issue problem when trying to run it in the terminal with both of the above commands both in the test directory and one level up. However, I was able to run the test in **Pycharm** by "right-clicking" on the file and then clicking on the `Run 'Unittests in test_calc.py'`. All of the test passed that way.

- The goal is not to write as many test as you can, it is to write GOOD test that take in to account for all edge cases.

- When you run the test, each "function/method" will be counted as one test, even though you are probably testing multiple edge case in that one test.

- You will see a `.` for each test that passes at the top of the return in the terminal when you run the test. In this example with the `test_calc.py` file, there are 4 test total and if one was to fail, say the 3rd test failed, it would return the `.`'s, like so: `..F.` and that tells you that it was the 3rd test that failed. Wherever the `F` is within the dots is the test that failed. Plus it will also tell you below that exactly what test failed and what the error is.

- If your code is raising an error if a certain condition is met, such as in this case with `raise ValueError` in the `calc.py` file, you can test that is working properly also with the following code:

    ```
    # This is one way to do it:
    self.assertRaises(ValueError, calc.divide, 10, 0)
        # param 1: the exception that is expected
        # param 2: the function to run but do not invoke
        # param 3: the first param for the function to run (calc.divide)
        # param 4: the second param for the function to run (calc.divide)
        # The reason it must be done this way is because otherwise the function
        #   will throw that value error and the test will not be ablt to run.
  
    # Another way to do the same thing:
    # By using a context manager (with) you can run the function like it
    #   normally would be ran.
    with self.assertRaises(ValueError):
        calc.divide(10, 0)
    ```

    - [Link to information on Context Manager in Python](https://book.pythontips.com/en/latest/context_managers.html)
    
### Testing `employee.py`

[Starts here in the video](https://youtu.be/6tNS--WetLI?t=1098)

- Notes on how to do the testing without the print statements are in the `snippets.txt` file from line 1 - line 61.

- Anytime that you see the same code over and over again, that is usually a good indicator that you want to try to simplify it. Programmers try to make their code DRY (Don't Repeat Yourself). This is where the `setUp` and `tearDown` methods come in.

- Notes on how to do the testing with the print statements and the `setUp` and `tearDown` methods are in the `snippets.txt` file from line 63 - line 137. The print statements are there just to show you how the test are being ran and in what order, they are not necessary.

- Never assume that all test run in order.

- Class Method: `@classmethod` We are working with the class rather than the instance of the class like we were with `self`. 
  
    - [Learn more about Class Methods in this video](https://youtu.be/rq8cL2XMM5M)
    
- The `setUpClass` and `tearDownClass` methods are very useful when you have something that you only want to run once at the beginning of the test or end of the test. 
  
    - An example of this might be if you are needing to populate a database to test against. This could save you on computing time because it will only have to read in the database once, and it will be available for all the tests when you add it to the set up class method. Then you can tear it down with the tear down class method.
    
- More comments and code in the `test_employee.py` file.
    
### Mocking

[Starts here in the video](https://youtu.be/6tNS--WetLI?t=1717)

This is a way to test your code if it is running through a server, and the server is down at the time of testing. Being that the purpose of this testing is to test the code, not the server availability.

- Need to have a method in your class to check if the server is currently running or not.

- Then need to use the `patch` method from `unittest.mock` as a context manager (`with`) or as a decorator (`@`) to "mock" an object while running a test and then that object is automatically restored after the test are done running.

- Mock objects record when they were called and with what values. Therefore, you can test to make sure that the correct url was called as well.

- More comments and code in the `test_employee.py` file from line 88 - line 117

### Closing Notes (Best Practices):

[Starts here in the video](https://youtu.be/6tNS--WetLI?t=2211)

- Tests should be isolated: Your test shouldn't rely on other tests or effect other tests. You should be able to run any test by itself, independent of the other tests.

- Test Driven Development: 
  
    - You write the test before you write the code. 
      
    - The idea behind this, is to think about what you want your code to do. 
      
    - Then write test to implement that behavior. 
      
    - Then watch the tests fail since it does not actually have any code to run against. 
      
    - Then write the code in a way that gets the tests to pass.
