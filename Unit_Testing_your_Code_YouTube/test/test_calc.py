"""
This file contains the logic for testing the calc.py file
"""

# Imports
import unittest
from Unit_Testing_your_Code_YouTube import calc


# Create a test class that inherits from unittest
class TestCalc(unittest.TestCase):

    # # One method of testing the add function in the calc.py file
    # # Need to make sure when naming that it starts with `test_` or it will not run
    # def test_add(self):
    #     # Get the result from the function
    #     result = calc.add(10, 5)
    #     # Assert if the result is equal to 15, which is the correct answer
    #     self.assertEqual(result, 15)

    # Another way to create a testing method for the add function
    def test_add(self):
        # Check if the return value is equal to the answer
        # Doing it this way, each line of code is testing a new edge case
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    # Create a testing method for the subtraction function
    def test_subtract(self):
        # Check if the return value is equal to the answer
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    # Create a testing method for the multiplication function
    def test_multiply(self):
        # Check if the return value is equal to the answer
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    # Create a testing method for the division function
    def test_divide(self):
        # Check if the return value is equal to the answer
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # # This will test that the `raise ValueError` is working properly in our code
        # # One way to do it is:
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # Or another way to do it is:
        with self.assertRaises(ValueError):
            # Call the function like you normally would
            calc.divide(10, 0)


# Allow us to run our test directly in the file
if __name__ == '__main__':
    # This will run all the tests in this file
    unittest.main()