"""Exception handling Example"""
# n = int(input("Enter your number. "))

# try:
#     print(10/n)

# except Exception as err:
#     print(f"Sorry there is an err as {err}")
# else:
#     print("Good there is no exception.")
# finally:
#     print("I will run No matter what.")

# print("Hurray!! I have done division.")

"""Raise Exception Example"""

age = int(input("Enter your age: "))


try:
    
    if age < 10 or age > 18:
      raise ValueError("Your age must be between 10 and 18")
    else:
      print("Wellcome to club")

except Exception as err:
   print(f"an error occured as {err}")

print("Tge Club will start soon")