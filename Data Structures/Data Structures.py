"""Data Structure 4 type of inbuilt data structure List, Tuple, Dictionary, set"""
"""List type: Mutable, Duplicate, Ordered, heterogenous """
"""List Indexing"""

# a = [1,2,3,4,5,6,7]
# print(a[0:5])

"""List Traversing and Method"""

# a = [12, 34, 45, 14, 47,77]

#First way using index

# for i in range(len(a)):
#     print(a[i])

#2nd way direct on values

# a = [12,3,4,67]

# for i in a:
#    print(i)

"""Difference between function and Method"""

# l = [1,2,3,4,5]

# l.append(6)
# l.append(7)
# l.insert(0,0)
# print(l)

"""Mutable List Example"""

# l =[1,2,3,4,5]

# l[1] = 10
# print(l)

"""Print positive and Negative element of an List"""
# l = [-34, 67, -8, 9, -10]

# print("Positive element are: ")
# for i in l:
#     if i >= 0:
#         print(i)

# print("Negative element are: ")
# for i in l:
#     if(i<0):
#         print(i)

"""Mean of list elements"""
# l = [1,2,3,4,5]

# sum =  0

# for i in l:

#     sum = sum + i

# print(sum/len(l))

"""Find the greatest element and print its index too."""

# l = [12, 34,67,89,99,100,8]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"Your largest number is {largest} at index {index}")        

"""Find the second greatest element"""

# l = [12, 16, 13, 19, 17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i

#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest, largest)

"""Check if list is sorted or not"""
# l = [12,13,14,15,11]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("Your list is not sorted.")
#         break
# else:
#     print("Your list is sorted.")

"""Tuple Power: Immutable, Duplicate, Ordered, Heterogenous"""

# a = (1,2,3,4,5,6,5,5,5,print(),'hello')

# index = a.index(6)
# count = a.count(5)

# print(count)

"""Concept of tuple unpacking"""

# a,b,c,d = (1,2,3,4)
# print(d)

"""Set Traversal"""
# a = {1,2,3,8,9,10,"Hello"}

# for i in a:
#     print(i)

"""Set methode Example"""
# a = {1,2,3,4,5,6,9,11}
# a.add(10)
# a.remove(5)
# a.pop()
# a.clear()
# print(a)

"""Set union, Intersection, Difference, symmetric Difference"""

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# s = a | b  #for union 
# s = a & b  #for intersection
# s = a - b  #for Differnece 
# s = a ^ b  #for Symmetric difference
# print(s)

"""Dictionary Example with CRUD Operation"""

# d = {10:100, 20:200, 30:300, 40:400}
# d[10] = 1000 #Updating
# d[50] = 500  #Creating
# del d[50]    #Deleting
# print(d)

"""Accessing Key and Values in dictionary"""

# d = {10:100,20:200,3:300,40:400,50:500}

# for i in d:
#     print(i)    #for index print
#     print(d[i])   #for value print


# a = [10,20,30,40,50,60]

# b = a

# b[0] = 100

# print(a)

"""Dictionary Deep Copy Example"""

d = {10:100,20:200,30:300,40:400,50:500}

print(d.items())

"""Question"""
"""Write a Python Script to merge two Python dictionaries."""

# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

"""Write a Python program to sum all the values in a dictionary."""

# d1 = {10:100,20:200,30:300}
# sum = 0
# for i in d1:
#     sum = sum + d1[i]
# print(sum)

"""Count the frequency of each element in a list"""

# a = [1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,7,8]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1
# print(d)

"""Write Python program to combine two dictionary by adding values for common keys"""

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)        