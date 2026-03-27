"""Conditional Statement
 .Conditional Statement in python decision-making by 
  executing different block of code based on conditions"""

# a = 6
# if a > 10:
#     print("I will do task number A.")
# else:
#     print("I will do task number B.")

"""Lets take a real life exmple to implement the conditional Statement"""
"""If my mom give me the Rs 10 then i will buy choco Bar and Rs > 10 then i will buy kitkat"""

# money = int(input("Please provide the money:- "))
# if money == 10:
#     print("I will buy choco bar.")
# else:
#     print("I will buy Kitkat.")

"""Next Example elif"""
# money = int(input("Enter the amount given by mom:- "))
# if money == 10:
#     print("I will have a choco bar")
# elif money == 20:
#     print("I will have a vanila Choco bar")
# else:
#     print("I will have Choclate bar")

"""Class Work Assignment"""

"""Take two number find the greatest one"""
# num1 = int(input("Enter the number first:"))
# num2 = int(input("Enter the number second:"))
# if num1 > num2:
#     print("{num1} is greatest than {num2}")
# elif num2 > num1:
#     print("{num2} is greater than {num1}")
# else:
#     print("Both number are equal")

"""Q2. Accept the gender from the user as char and print 
the respective greeting Message
Ex: Good Morning Sir(On the basis of gender)"""

# gender = input("Please enter the gender (M or F):-")
# if gender == 'M':
#     print("Good Morning Sir!!")
# elif gender == 'F':
#     print("Good Morining Mam!!")
# else:
#     print("You have enter the wrong the character, Please write either M or F.")

"""Qno.3: Accept an integer and check whether 
it is an even number or odd"""

# num1 = int(input("Enter the number:"))
# if num1%2 == 0:
#     print("{num1} is Even number.")
# else:
#     print("{num1} is Odd number.")


"""Qno.4: Accept name and age from the user. 
check if the user is valid voter or not"""

# name = input("Enter your name: ")
# age = int(input("Enter your Age:"))

# if age>= 18:
#     print(f"Hurray {name} you are a valid voter!!")
# else:
#     print(f"Sorry to say you {name} ! you are not valid voter!!")

"""Qno.5: Accept a year and check if it a leap year or not
(google to find oyt the what is leap year)"""

# year = int(input("Enter the year:"))
# if year % 100 == 0 or year % 400 == 0:
#     print("{year} is a leap year.")
# elif year % 100 != 0 or year % 4 == 0:
#     print("{year} is leap year")
# else:
#     print("{year} is not leap year.")

"""
if - elif ladder
.You can also create if elif ladder using multiple conditions of elif
.For understanding solve this question
.take the input of temprature in celsius.
. Below 0°C -> "Freezing Cold"
. 0°C to 10°C -> "Very Cold"
. 10°C to 20°C -> "Cold"
. 20°C to 30°C -> "Pleasent"
. 30°C to 40°C -> "Hot"
. Above 40°C -> "Very Hot"
"""

# temp = int(input("Enter the Temprature: "))
# if temp < 0:
#     print("Freezing Point")
# elif temp >= 0 and temp < 10:
#     print("Very Cold")

# elif temp >= 10 and temp < 20:
#     print("Cold")

# elif temp >= 20 and temp < 30:
#     print("Pleasent")

# elif temp >= 30 and temp < 40:
#     print("Hot")

# else:
#     print("Very hot")
