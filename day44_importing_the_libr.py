# -*- coding: utf-8 -*-
"""day44 importing the libr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-WgKjTtf0HWbDT0jCPDm1GYx0c1lHOly
"""

# importing the  entier library:
import math

# importing with an alias:
import numpy as np

#Importing a specific  items from a library:
from datetime import datetime

# Importing the everything from the module(not recommeded for large libraries)
from itertools import permutations as perms

# importing the  specific item and everyting else with an alias:
from random import randint

# conditional import based on python version:\
import sys
if sys.version_info.major ==3:
  from urllib.request import urlopen
else:
  from urllib import urlopen

# Importing the submodul
import matplotlib.pyplot as plt

# importing a specific class from a module:
from sklearn.linear_model import  LinearRegression

# Importing  all classes from a module
from sklearn.linear_model import*

# importing the module and using an alias:

import requests as req

# Importing a module and specific items:
from bs4 import BeautifulSoup, NavigableString

import turtle

def draw_heart():
    t = turtle.Turtle()
    t.fillcolor("red")
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

def write_text():
    t = turtle.Turtle()
    t.penup()
    t.color("white")
    t.goto(0, -50)
    t.write("Punith BS", align="center", font=("Arial", 14, "bold"))

def main():
    turtle.bgcolor("black")
    draw_heart()
    write_text()
    turtle.done()

if __name__ == "__main__":
    main()

# Importing  a module  dynamically:
module_name="requests"
my_module=__import__(module_name)

import my_custom_module as mcm

import my_custom_module as mcm

# Importing a module from a parent dictionary:
import sys
sys.path.append("path/to/parent_dictionary")
from module import item

