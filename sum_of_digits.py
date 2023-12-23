num = int(input("Enter a number :"))
ssum = 0
nnum = num
while (nnum != 0):
    digit = nnum%10;
    nnum = nnum//10
    ssum += digit
print("Sum of the digits of number", num, "is :", ssum)