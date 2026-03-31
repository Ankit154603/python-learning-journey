#For Loop
# for i in range(1, 21, 1):
#  print(i)

"""Order"""
# for i in range(20, 51):
#  print(i)

"""Reverse Order......  16 to 1"""
# for i in range(16, 0, -1):
#  print(i)

"""Negative Step -5 to -15"""
# for i in range(-5,-16, -1):
#  print(i)

"""Lets print of table of 5"""
# for i in range(5,51,5):
#  print(i)

"""Take input from the user for any table multiplication"""
# n = int(input("Which table you want:"))
# for i in range(n,(n*10)+1,n):
#  print(i)

"""Print Hello Word 100 Times"""
# n = "hello words"
# for(int i = 1; i < n; i++)
# print(i)

"""Print character"""
# a = "Jai Shiya Ram"
# for i in range(len(a)):
#  print(a[i])

"""Another way to print the character"""
# a = "Jaijaijai Shiya Ram"
# for i in a:
#  print(i)

"""Break loop"""
# for i in range(1, 21):
#  if i == 15:
#  break
#  print(i)

"""Continue Loop"""
# for i in range(1, 21):
#  if i == 19:
#  continue
#  print(i) #so continue skip 19 an write upto less than 21 i.e 20

"""Else Loop"""
# for i in range(1,21):
#  if i == 45:
#  print("Break Statement is Executed.")
#  break
#  print(i)
# else:
#  print("Break Statement is not executed.")

"""Loop Questions"""
"""Q1. Accept an integer and print hello world n times"""

# n = int(input("Enter the n inetger:- "))
# for i in range(n):
#  print("hello Words")

"""Print natural number up to n"""
# n = int(input("Enter Natural Number you want to print: "))
# for i in range(1,n):
#  print(i)

"""Reverse for loop.print n to 1"""
# n = int(input("Enter the value of n: "))
# for i in range(n,0,-1):
#  print(i)

"""Take a number as input and print its table."""
# num = int(input("Enter the number as input: "))
# for i in range(num,(num*10)+1,num):
#  print(i)

"""Sum up to n terms"""
# n = int(input("Enter the number you want sum: "))
# sum = 0
# for i in range(1,n+1):
#  sum = sum + i

# print(f"Your sum is {sum}")

"""Factorial of a number"""
# n = int(input("Enter the factorial number:"))
# fact = 1
# for i in range(1,n+1):
#  fact = fact * i
# print(f"Factorial of the number is {fact}")

"""Print the sum of all even and odd number in a range separately"""
# n = int(input("Enter the Even or Odd Number:"))
# even = 0
# odd = 0
# for i in range(1, n+1):
#  if i%2 == 0:
#  even = even + i
#  else:
#  odd = odd + i

# print(f"Your even and odd sum are {even}, {odd}")

"""Print all the factor of a number"""
# n = int(input("Which number you want to factor: "))
# for i in range(1, n+1):
#  if n%i == 0:
#  print(i)

"""Accept a number and check if it a perfect number or not.
A number whose sum of factors is equal tot he number itself
Ex: 6 = 1,2,3 = 6"""

# n = int(input("Check ypu number is Perfect or not: "))
# sum = 0
# for i in range(1, n):
#  if n%i == 0:
#  sum = sum + i
# print(sum)

# if sum == n:
#  print("Your number is perfect number.")
# else:
#  print("Your number is not perfect number.")

"""Check whether number is prime or not"""

# n = int(input("Check you number is prime or not: "))
# count = 0
# for i in range(1, n+1):
#  if n%i == 0:
#  count = count + 1

# if count == 2:
#  print("Your number is prime.")
# else:
#  print("your number is not prime.")

"""Reverse a string without using in build functions"""

# a = "Jiaj"
# b = ""
# for i in range(len(a)-1,-1,-1):
#  b = b + a[i]
# print(b)

"""Chech a string is palindrome or not """
# a = "NAMAN"
# b = ""
# for i in range(len(a)-1,-1,-1):
#  b = b + a[i]
# if b == a:
#  print("Tha number is pallindrome number.")
# else:
#  print("The number is not pallindrome number.")

"""Count all letters, digits, and special symbols from a given string
Given: str1 = "P@#yn26at^&i5ve"
Expected Outcome:
    Total counts of chars, digits, and symbols
    Chars = 8
    Digits = 3
    Symbols =4 """

    # a = "numpypanda127643(@#%^&*)"

    # char = 0
    # dig = 0
    # spchr = 0

    # for i in a:
    #  if i.isdigit():
    #  dig += 1
    #  elif i.isalpha():
    #  char += 1
    #  else:
    #  spchr += 1
    # print(f"your digit are {dig}\nyour character are {char}\nyour special
    # character are {spchr}")

    """While Loop Questions:Separate each digit of a number and print it on the new line"""

    # a = int(input("Tell your numnber: "))

    # while a>0:
    #  print(a%10)
    #  a = a// 10

    """Accept a number and print its reverse."""
    # a = int(input("Entert your number: "))
    # rev = 0
    # while a > 0:
    #  rev = rev * 10 + a % 10
    #  a = a// 10
    # print(rev)

    """Accept a number and check if its a palindrome number
    (if number and its reverse are equal)"""

    # a = int(input("Enter your number: "))
    # copy = a
    # rev = 0
    # while a > 0:
    #  rev = rev * 10 + a % 10
    #  a = a // 10

    # if copy == rev:
    #  print("Number is pallindrom.")
    # else:
    #  print("number is not pallindrome.")

    """Create a random number guessing game with python"""


# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("please guess your number between 1-10: "))

#     if num == guess:
#             tries += 1
#             print("Your are right youb guessed the number is {tries}.")
#             break

#     elif num < guess:
#             print("go a little lower")
#             tries += 1

#     elif num > guess:
#             print("go little higher")
#             tries += 1

#     else:
#             tries += 1
#             print("your are wrong.")