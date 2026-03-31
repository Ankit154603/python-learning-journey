"""Object Oriented Programming"""
"""Constructor"""

# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Your object details are {self.material}, {self.zips}, {self.pockets}")

# rebook = Factory("leather",3,2)

# campus = Factory("nylon",4,4)

# rebook.show()

"""Attribute and Methods"""

# class Animal:
#     def __init__(self,age):
#         self.age = age  #instance attribute
    
#     def show(self):   #instance method
#         print(f"how are you! your agger is {self.age}")
    
#     @classmethod
#     def hello(cls):  #cls belong to class object
#         print("how are you from clas method {cls.age}")

#     @staticmethod
#     def static():
#         print("how are you")

# obj = Animal(12)
# obj.show()

"""Four Pillar"""
"""1. Inheritance"""
 
# class Factorymumbai:
#     a = "Hello i am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):
#     pass

# obj = Factorymumbai()

# obj2 = Factorypune()

# obj2.hello()

"""Constructor in Inheritance"""

# class Animal:
#     def __int__(self,name):
#         self.name = name
#     def show(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"Hello your name is {self.name}, {self.age}")

# animal = Animal("lion")
# person1 = Human("akarsg", 23)
# person1.show()

"""Type of Inheritance"""
# class Animal:
#     name1 = "lion"
# class Human:
#     name2 = "harsh"
# class Robots(Animal,Human):
#     name3 = "charli23"

# obj = Robots()

# print(obj.name3)

# class Animal:
#     def __init__(self,name):
#         pass
# class Human:
#     def __init__(self,name,age):
#         pass
# class Robots(Human,Animal):
#     name3 = "charli23"

# obj = Robots()    #MRO

"""MultiLevel Inheritance"""

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory(Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color

# class Punefactory(BhopalFactory):
#      def __init__(self, material, zips, color, pockets):
#          super().__init__(material, zips, color)
#          self.pockets = pockets

# obj = Punefactory()


"""2. Pillar-----Polymorphism"""
"""1. Overrriding Exmple"""

# class Animal:
#     def show2(self):
#         print("Hello")

# class Human(Animal):
#     def show(self):
#         print("Hello how are you")

# obj = Human()
# obj.show()


"""2. Duck Typing"""
# class Animal:
#     def show(self):
#         print("Hello from Animal")

# class Human:
#     def show(self):
#         print("hello from human")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()

"""3. Encapsulation"""

# class Factory:

#     _a ="pune"

#     def show(self):
#         print("hello i am pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().a)


# obj = Bhopal()
# obj.show2()

"""Private method and Attribute"""
# class Factory:

#     __a ="pune"

#     def __show(self):
#         print("hello i am pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().__a)


# obj = Bhopal()
# obj.show2()


"""4. Abstraction"""

# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("I a have created")

#     def area(self):
#         print("I a have created this")

# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius

#     def perimeter(self):
#         print("I a have created")

#     def area(self):
#         print("I a have created this")

# obj = Circle(7)
# obj2 = Square(12)

"""Dunder Method"""

# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return(f"Hello how are you! and your nam is {self.name}")
#     def __add__(self, other):
#         return f"your sum of ages are {self.age + other.age}"

# obj1 = Animal("lion",12)
# obj2 = Animal("dolphin",14)

# print(obj1 + obj2)

"""Decorater """

# class Animal:
#     @property
#     def show(self):
#         print("hello how are you.")

# obj = Animal()

# obj.show

"""Decorate Advance Example"""

# def decorate(func):
#     def wrapper(a,b):
#         print("Thank you hope your sum is correct!!")
#         func(a,b)
#         print("Thank you i hope you like it")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"Your total sum is {a + b} ")

# addition(12,12)

"""Args and Kwargs"""

# def information(**kwargs):
#     print("Your information is \n\n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Ram", age = 16, designation = "God of god")

"""Lsit Dictionary and set comphrehension"""

# l = [i for i in range(1,21) if i % 2 == 0]   # Listn Compherension
# print(l)

"""List Comphrension"""

# l = {i : i**2 for i in range(1,10)}  #Dictionary Compherension
# print(l)

"""Lambda functions"""

# addition = lambda a : "even" if a % 2 == 0 else "odd"

# print(addition(12))

"""Map filter"""

# a =[1,2,3,4,5]

# result = map( lambda x : x*2,a)

# print(list(result))


"""Filter"""

# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# a = [1,2,3,4,5,6,7,8,9]

# result = filter(lambda x : True if x % 2 == 0 else False, a)

# print(list(result))


"""Module and Packages"""

import maths

print(maths.addition(12,12))