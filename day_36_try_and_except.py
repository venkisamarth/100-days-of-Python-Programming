# -*- coding: utf-8 -*-
"""day 36 try and  Except.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18qEVBNZq2ohskHGRrqZT8ucNIh8G0S_-
"""

#Basic example :
try:
  result=10/0
except ZeroDivisionError as e:
  result ="Cannot divide by Zero"
print(result)

# Handling  Indexing
try:
   my_list=[1,2,3,4]
   print(my_list[5])
except IndexError as e:
  print(f"Error: {e}")

# HAndling FileNotFoundError
try:
  with open("nonexistendt_file.txt","r") as file:
    content=file.read()
except FileNotFoundError as e:
  print(F"Error: {e}")

# Handiling type Error:
try:
    result = int("abc")
except TypeError as e:
    print(f"Error: {e}")

# Handling the  Value Error:
try:
  num=int("123abc")
except ValueError as e:
  print(f"Error: {e}")

# Handiling the key Error
try:
  my_dict={"key":"value"}
  print(my_dict["nonexistent_key"])
except KeyError as e:
  print(f"Error: {e}")

# Handiling the Assertion Error:
try:
  assert 2+2==5, "Math is not correct!"
except AssertionError as e:
  print(f"Error:{e}")

# Handiling the attributionError:
class MyClass:
  pass
try:
  obj =MyClass()
  obj.method()
except AttributeError as e :
  print(f"Error: {e}")

# Handling the NameError:
try:
  print(undefined_varible)
except NameError as e:
  print(f"Error: {e}")

# Handiling IOError:
try:

  with open("/nonexistent_path/file.txt","r")as file:
    content  =file.read()
except IOError as e:
  print(f"Error:{e}")

# Handling the memoryError:
try:
  data=[1]*10*8 # this may lead to a memoryError
except MemoryError as e:
  print(f"Error: {e}")

# Handling JSOnDEcodeError:
import json
try:
  data=json.loads("invalid_json")
except json.JSONDecodeError as e:
  print(f"Error:{e}")

# Handling filneNotFound with else block:
try:
  with open("existing_file.txt","r") as file:
      content =file.read()
except FileNotFoundError as e:
  print(f"Error:{e}")
else:
  print('File read successfully.')

# Handiling the multiple Exceptions:
try:
  result=10/0
except (ZeroDivisionError,TypeError) as e:
  print(f"Error: {e}")

# Handling the any exception:
try:
  reault=100/0
except Exception as e:
  print(f"Error: {e}")

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Custom Error: {e}")

# Handling the zero Divison error with finnaly block:
try:
  result=10/0
except ZeroDivisionError as e:
  print(f"Error: {e}")
finally:
  print("This block always executes.")

# Raising an Exception:
try:
  raise ValueError("This is a raised exception.")
except ValueError as e:
  print(f"Error: {e}")

# Handling FileNotFoundError with FileNOtFound as e:
try:
    with open("existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

