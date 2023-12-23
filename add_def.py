from re import S


def calcsum(x, y):
    s = x+y
    return s

num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
sum = calcsum(num1, num2)
print("Sum of two given numbers is", sum)