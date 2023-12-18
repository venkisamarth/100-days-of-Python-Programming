# -*- coding: utf-8 -*-
"""day37 finally block in python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P6CFvOhdzknxUhouJH7MK0lVuIH-gcKa
"""

try:
  print("This Block")
except Exception as e:
  print(f"Error: {e}")

finally:
  print("finnaly block")

# Handling the division by Zero with finally:
try:
  result=10/0
except ZeroDivisionError as e:
  print(f"Error:[e]")
finally:
  print("Finnaly block")

# Readiing file with Finally:
try:
  with open("existring_file.txt","r") as file:
    content =file.read()
except FileNotFoundError as e:
  print(f"Error:{e}")
finally:
  print("Finally block")

# from typing import final
# Database Connection Example:
try:
  raise Exception("Database connection error")
except Exception as e:
  print(f"Error:{e}")
finally:
  print("Closing database connection")

# Handling Multiple Exception error:
try:
  result=10/0
except (ZeroDivisionError,TypeError) as e:
  print(f"Error: {e}")
finally:
  print("finnally block")

# Nested Try_Except-Finnaly Blocks:
try:
  try:
    print("Inner try block")
  except Exception as e:
    print(f"Inner Error: {e}")
  finally:
    print("Inner finally block")
except Exception as e:
  print(f"Out Error: {e}")
finally:
    print("outer finally block")

# Handling Assertion Error Finally:
try:
  assert 2+3==5, "Math is not correct!"
except AssertionError as e:
  print(f"Error:{e}")
finally:
  print("Finally Block")

# Handling FileNotFound with Else and Finally:
try:
    with open("existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    print("File read successfully.")
finally:
    print("Finally block")

# Raising Exception with Finally:
try:
   raise ValueError("This is a raised exception.")
except ValueError as e:
  print(f"Error: {e}")
finally:
  print("Finnaly block")

# Using finally for cleanup:
try:
  file=open("temp_file.txt","w")
  file.write("some data")
finally:
  file.close()
  print('File closed')

# Using finally in loop:
try:
  for i in range(5):
    print(10/i)
except ZeroDivisionError as e:
  print(f"Error: {e}")
finally:
  print('Loop completed')

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Custom Error: {e}")
finally:
    print("Finally block")

