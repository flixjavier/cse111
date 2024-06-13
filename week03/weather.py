""" def main():
  deposit(1)
  test_min() """


#You can uses pytest to test your code
""" pytest is a third-party Python module that makes it easy to write and run test functions. """

""" Because computers approximate floating-point numbers, we must carefully compare them in our test functions """

"""  It is a bad practice to check if floating-point numbers are equal using just the equality operator (==). A better way to compare two floating-point numbers is to subtract them and check if their difference is small """

""" The tolerance is the maximum difference between two floating-point numbers that the programmer will allow and still consider the numbers to be equal."""

""" The pytest module contains a function named approx to help us compare floating-point numbers more easily. The approx function* compares two floating-point numbers and returns True if they are equal within an appropriate tolerance. """


""" How to Test a Function
To test a function you should do the following:

Write a function that is part of your normal Python program.
Think about different parameter values that will cause the computer to execute all the code in your function and will possibly cause your function to fail or return an incorrect result.
In a separate Python file, write a test function that calls your program function and uses an assert statement to automatically verify that the value returned from your program function is correct.
Use pytest to run the test function.
Read the output of pytest and use that output to help you find and fix mistakes in both your program function and test function. """

""" def deposit(amount):
  assert amount > 0 #if amount is zero or negative, the program will break and send an assertion error
def test_min():
  assert min(7, -3, 0, 2) == -3

main() """

def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return cels