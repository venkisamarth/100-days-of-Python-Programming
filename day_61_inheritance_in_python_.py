# -*- coding: utf-8 -*-
"""day 61 Inheritance in python .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/102DyzczFUSVkN3XKHbDeKy2bcAXCn59R

When a class derives from another class. The child class will inherit all the public  and protected properties and method from the parent class. In addition, it can have its own properties and methods, this is called as inheritance.

Python inheritance Syntax
"""

class BaseClass:
  Body of base Class
class DerivedClass(BaseClass):
  Body of derived class

"""Derived class inherits featurs  form the base where new features can be added to it. This results in re-usability of code.

Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

Types of inheritance:



Single inheritance

Multiple inheritance

Multilevel inheritance

Hierarchical Inheritance

Hybrid Inheritance

We will see the explaination and example of each type of inheritance in the later tutorials
"""

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Derived class (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Create instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call methods
animal.speak()  # Output: Generic Animal makes a sound
dog.speak()     # Output: Buddy barks
cat.speak()     # Output: Whiskers meows
