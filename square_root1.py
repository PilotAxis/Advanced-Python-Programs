# Program to find square root of a number...

a = int(input("Enter a number :")) #input() used to take input from user
root = a**(1/2) #** means here power that is a raised to power 1/2
print("The square root of the number", a, "is :", root)
print("end")

#we can also use math module to find the square root of the number...

import math
root1 = math.sqrt(a)
print("The square root of the number", a, "is :", root1)
