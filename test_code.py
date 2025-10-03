"""This code is here to test your calculator program so you can make sure it meets all the required specifications of the assignment.
Remember that when I grade your code I do not use this same autograder.
It is meerly here for you to know what your grade is likely to be assuming you followed instructions correctly to pass the tests."""

import pytest
import random

def test_add():
  try: 
    from Calculator_code import add
    num1 = random.randint(-100,100)
    num2 = random.randint(-100, 100)
    result = add(num1, num2)
    assert result == num1 + num2
  except SyntaxError as e:
    print(f"error importing add(): {e}")
def main():
  test_add()

if __name__ == "__main__":
    main()
