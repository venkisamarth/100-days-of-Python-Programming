# -*- coding: utf-8 -*-
"""day57 Object and class in python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oruW6Azot7PukEaDy3XtxAPmyOPnf15a

Object and the class in python

A Class is a bluprint or a template for creating object, providing initial values for state ( member variales or attributes), and implementations of behavior( members functios or methods). The user-defined objects are created using the class keyword
"""

# creating the class :
class Details:
  name="Rohan"
  age=20

# creeatirng the object:
#Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
obj1=Details()

#Now we can print values:
#Example:
class Details:
  name="Rohan"
  age=20
obj1==Details()
print(obj1.name)
print(obj1.age)

class Person:
  name="Harry"
  occupation="software Developer"
  networt=10
  def info(self):
    print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()
c=Person()
a.name="Shubham"
a.occupation="Accountant"

b.name="Nitika"
b.occupation="HR"


# print(a.name,a.occupation)
a.info()
b.info()
c.info()

# Simple Person Class
class Person:
  def __init__(self, name, age):
    self.name=name
    self.age=age
# creating objects of the Person class
Person1=Person("Alice",25)
Person2=Person("Bob",30)
# Accessing object attributes
print(Person1.name)
print(Person2.age)

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        self.speed -= speed_decrease

# Create objects of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Using methods of the Car class
car1.accelerate(20)
car2.brake(10)

print(car1.speed)  # Output: 20
print(car2.speed)  # Output: -10

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

# Create objects of the BankAccount class
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob")

# Using methods of the BankAccount class
account1.withdraw(500)
account2.deposit(200)

print(account1.balance)  # Output: 500
print(account2.balance)  # Output: 200

class Book:
    genre = "Fiction"

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create objects of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Accessing class attribute and object attributes
print(Book.genre)    # Output: Fiction
print(book1.title)   # Output: The Great Gatsby
print(book2.author)  # Output: Harper Lee

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Abstract method

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(species="Dog")
        self.name = name
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Create objects of the Dog class
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "Poodle")

# Using inherited methods
print(dog1.make_sound())  # Output: Woof!
print(dog2.species)       # Output: Dog

