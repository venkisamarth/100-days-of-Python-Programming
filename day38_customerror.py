# -*- coding: utf-8 -*-
"""day38 customError.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U_3JJraTPmy5i2Aj_o5Z5jSzfdM6ea6t
"""

# Basic custom Error:
class CustomError(Exception):
  pass
try:
    raise CustomError("This is a custom Error.")
except CustomError as e:
  print(f"Cuught an  Exception: {e}")

# CustomeError with Specific Message:
class CustomError(Exception):
    def __init__(self, message="This is a custom error with a specific message."):
        self.message = message
        super().__init__(self.message)

try:
  raise CustomError()
except CustomError as e:
  print(f"Caught exception: {e}")

# CustomError With default Message:
class CustomError(Exception):
  def __init__self(self,message="Default sustom error message."):
    self.Message=message
    super().__init__(self.message)
try:
  raise CustomError()
except CustomError as e:
  print(f"Caught an exception: {e}")

# Cutom Errror with Parameters:
class CustomError(Exception):
  def __init__(self,code,message):
    self.code=code
    self.message =message
    self.message=message
    super().__init__(f"Error {code}:{message}")
try:
  raise CustomError(404,"Notfound")
except CustomError as e:
  print(f"Caught an exception:{e}")

# Custom Error with formatting:
class CustomError(Exception):
  def __init__(self,*args):
    self.args=args
    super().__init__(f"Custom error with arguments: {args}")
try:
  raise CustomError(1,"abc",[3,4])
except CustomError as e:
  print(f"Caught an exception: {e}")

# Hierarchical Custom Errors:
class BaseError(Exception):
    pass

class CustomError(BaseError):
    def __init__(self, message="This is a custom error."):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This error inherits from BaseError.")
except BaseError as e:
    print(f"Caught a base exception: {e}")
except CustomError as e:
    print(f"Caught a custom exception: {e}")

class CustomError(Exception):
    def __init__(self, message="Custom error."):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Caught an exception: {e}")
finally:
    print("Cleanup code executed.")

# custom Error with Logging:
import logging

class CustomError(Exception):
    def __init__(self, message="Custom error."):
        self.message = message
        super().__init__(self.message)
        logging.error(f"An error occurred: {message}")

try:
    raise CustomError("This is a custom error with logging.")
except CustomError as e:
    print(f"Caught an exception: {e}")

class CustomError(Exception):
  def __init__(self,message="custom error"):
    self.message=message
    super().__init__(self.message)
def my_function():
  raise CustomError("Error in my_function.")
try:
  my_function()
except CustomError as e:
  print(f"Caught an exception: {e}")

#  custom Error with Additonal Inforamtion:

class CustomError(Exception):
    def __init__(self, code, message, details=None):
        self.code = code
        self.message = message
        self.details = details
        super().__init__(f"Error {code}: {message}")

try:
    raise CustomError(500, "Internal Server Error", {"reason": "Unknown"})
except CustomError as e:
    print(f"Caught an exception: {e}")

