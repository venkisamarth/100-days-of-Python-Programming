# print(): 
print(" this is the print built in function")
# input("Enter the number")

# abs(): 
print(abs(5))
print(abs(-3.14))
print(abs(-18))
print(abs(0))
print(abs(-75))


# all(): 
print(all([True,True,False]))
print(all([1,2,3,4,5]))
print(all([]))
list1=[True,True,True]
print(all(list1))

list2=[True,True,True]
print(all(list2))

list3=[1,2,3,4,5,6]
print(all(list3))

list3=[1,2,3,4,5,6]
print(all(list3))

list4=[]
print(all(list4))
# ArithmeticError
# AssertionError
# AttributeError
# BaseException
# BaseExceptionGroup
# BlockingIOError
# BrokenPipeError
# BufferError
# BytesWarning
# ChildProcessError
# ConnectionAbortedError
# ConnectionError
# ConnectionRefusedError
# ConnectionResetError
# DeprecationWarning
# EOFError
# EncodingWarning
# EnvironmentError
# Exception
# ExceptionGroup
# FileExistsError
# FileNotFoundError
# FloatingPointError
# FutureWarning
# GeneratorExit
# IOError
# ImportError
# ImportWarning
# IndentationError
# IndexError
# InterruptedError
# IsADirectoryError
# KeyError
# KeyboardInterrupt
# LookupError
# MemoryError
# ModuleNotFoundError
# NameError
# NotADirectoryError
# NotImplementedError
# OSError
# OverflowError
# PendingDeprecationWarning
# PermissionError
# ProcessLookupError
# RecursionError
# ReferenceError
# ResourceWarning
# RuntimeError
# RuntimeWarning
# StopAsyncIteration
# StopIteration
# SyntaxError
# SyntaxWarning
# SystemError
# SystemExit
# TabError
# TimeoutError
# TypeError
# UnboundLocalError
# UnicodeDecodeError
# UnicodeEncodeError
# UnicodeError
# UnicodeTranslateError
# UnicodeWarning
# UserWarning
# ValueError
# Warning
# WindowsError
# ZeroDivisionError
# __build_class__
# __import__
# __loader__
# abs
# aiter
# all
# anext
# any
# ascii
# bin
# bool
# breakpoint
# bytearray
# bytes
# callable
# chr
# classmethod
# compile
# complex
# copyright
# credits
# delattr
# dict
# dir
# divmod
# enumerate
# eval
# exec
# exit
# filter
# float
# format
# frozenset
# getattr
# globals
# hasattr
# hash
# help
# hex
# id
# input
# int
# isinstance
# issubclass
# iter
# len
# license
# list
# locals
# map
# max
# memoryview
# min
# next
# object
# oct
# open
# ord
# pow
# print
# property
# quit
# range
# repr
# reversed
# round
# set
# setattr
# slice
# sorted
# staticmethod
# str
# sum
# super
# tuple
# type
# vars
# zip
print("anny function in python ")
list1=[False ,False,False]
print(any(list1))

list2=[False,True,False]
print(any(list2))

list3=[0,0,0]
print(any(list3))

list4=["venki","34",3,4]
print(any(list4))

print(any([]))


print("ascii()")

print(ascii("hello"))

print(ascii("E"))
print(ascii("232"))
print(ascii(34))

print(ascii("V"))

print(ascii('E'))
print(ascii('😊'))
# Example 3
print(ascii('привет')) 
print(ascii('€'))


print('tuple inbult function')
my_list=[1,2,2,3,4]
my_tuple=(tuple(my_list))
print(my_tuple)

empty_tuple=tuple()
print(empty_tuple)

my_string ="hello"
tuple_from_string=tuple(my_string)
print(tuple_from_string)

#using the paking and unpaking  tuple 
x=1
y=2
my_tuple=x,y
print(my_tuple)
# creating a tuple wiwth repeted elements : 
repeted_tuple=(0,)*5
print(repeted_tuple)


print("Example for type()")

#checking the type of a variable: 
x=10 
print(type(x))

#checking the type of a string 
my_string ="hello"
print(type(my_string))

#checking the type of dictionary: 
my_dict={"a": 1,"b":2}
print(type(my_dict))

#checking the type of a function
def my_func(): 
    return "hello"
print(type(my_func))

print("Ecample for vars()")
# vars() returns "__dict__" attrubute of an object which contains its namespace 
#accssing avriable in the current namespace 
x=10 
y=20 
print(vars())

# accessing variable in a class namspace 
class myClass:
    def __init__(self): 
        self.a=1 
        self.b=2

obj1=myClass()
print(vars(obj1))

# accessing vavraible in a module namespace 
import math  
print(vars(math))

# Accessing variable in afunciton namespace 
def my_funciton(): 
    x=10 
    y=20 
    print(vars())
my_funciton()
print('Exmaple for the zip fucniton ')
# combaing two list 
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
zipped =zip(list1,list2)
print(list(zipped))

#ziping with uneven lenght list 
list1=[1,2,3,4]
list2=["a","b"]
zipped=zip(list1,list2)
print(list(zipped))

# Zip with string and list 
string ="hello"
list1=[1,2,3,4,5]
zipped=(zip(string,list1))
print(list(zipped))

#zip with tuple: 
tuple1=(1,2,3,4,5)
tuple2=("a","b","c")
zipped=zip(tuple1,tuple2)
print(list(zipped))

#unziping a zipped list 
zipped_list =[(1,"a"),(2,"b"),(3,"c")]
unzipped=zip(*zipped_list)
print(list(unzipped))

print("Example  for sorted()")
# sorting a list of integers: 
numbers=[3,3,4,5,3,2,2]
sorted_numbers=sorted(numbers)
print(sorted_numbers)

#Sorting the list of string 
fruits=["apple","banna","orange","kiwi"]
sorted_fruits=sorted(fruits)
print(sorted_fruits)
# sorting in reverse order 
numbers =[4,3,4,5,6]
reverse_sorted=sorted(numbers,reverse=True)
print(reverse_sorted)

#Soritng  based on custom jey function
words =["banana","apple","kiwi","orage"]
sorted_words=sorted(words,key=len)
print(sorted_words)

#Sorted dictaiony by values: 
score={"Alice":90,"Bob":80,"Charli":95}
sorted_scores=sorted(score.items(),key=lambda x:x[1],reverse=True)
print(sorted_scores)

print("Example of the staticmethod()")
