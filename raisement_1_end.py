import math
num = int(input('Enter a number :'))
ln = len(str(num))
lst = num%10
fst = num // math.pow(10, ln - 1)
print('Length of given number', num, "is", ln)
print("The first digit is :", fst)
print('The last digit is :', lst)
print("First digit raised to the length :",\
    math.pow(fst, ln))
print("Last digit raised to the length :",\
    math.pow(lst, ln))
