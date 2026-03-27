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
money = int(input("Enter the amount given by mom:- "))
if money == 10:
    print("I will have a choco bar")
elif money == 20:
    print("I will have a vanila Choco bar")
else:
    print("I will have Choclate bar")
