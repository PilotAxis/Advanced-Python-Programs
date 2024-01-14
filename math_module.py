from math import factorial, gcd
num = int(input("Enter a number :"))
print("Factorial of", num, "is :", end = " ")
print(factorial(num))
gcd_1 = int(input("Enter 1st number :"))
gcd_2 = int(input("Enter 2nd number :"))
print("GCD of", gcd_1, "and", gcd_2, "is :", end = " ")
print(gcd(gcd_1, gcd_2))
