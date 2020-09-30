"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

#print(type(pi))
#print(pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
"""
i = random.randint(0, 100)
i = 50

if i<50:
    print ("I am less than 50")
elif i>50:
    print ("I am greater than 50") 
else:
    print ("I am 50!")
"""


# TODO: Write a conditional that prints the color of the picked fruit

"""
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == "orange":
    print ("ORANGE")
elif picked_fruit=="strawberry":
    print ("STRAWB")
elif picked_fruit=="banana":
    print ("BANA")
"""

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.



def multipl (a,b):
    return (a*b)

"""
a = 5
b = 4
print (multipl(a,b))
"""


# TODO: Now call the function a few times to calculate the following answers


print("12 x 96 =", multipl(12,96))

print("48 x 17 =", multipl(48,17))

print("196523 x 87323 =", multipl(196523,87323))
