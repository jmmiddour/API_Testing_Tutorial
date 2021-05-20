import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        """
        Method to instantiate the Class with the following parameters.
            :param first: str: employee's first name
            :param last: str: employee's last name
            :param pay: str: employee's current pay rate
        """
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """
        Method to return the employee's email in the specified format.
            :return: str: email as '<first name>.<last name>@email.com'
        """
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """
        Method to return the employee's full name in the specified format.
            :return: str: full name as '<first name> <last name>'
        """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """
        Method to increase the employee's current pay by the raise amount
            :return: int: employee's new current pay rate after raise
        """
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        """
        Method to check if the server is currently running,
            need this information to know if we have to create mocking
            data to run the test code.
            :param month: str: month of the year requested
            :return: str: Either the text from the server or
                            'Bad Response' if the server is down.
        """
        # Connects to the server and gets the data
        response = requests.get(f'http://company.com/{self.last}/{month}')

        # Check if the server is running currently
        if response.ok:
            # Returns the response text
            return response.text

        else:  # Otherwise, the server is not running
            # Return message letting you know the server is down currently
            return 'Bad Response!'