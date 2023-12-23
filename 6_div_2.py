num = int(input("Enter a 6-digit number :"))
if num < 100000 or num > 999999 :
    print('Please enter a 6-digit number.')
else:
    n1 = num%100
    int1 = num // 100
    n2 = int1 % 100
    int2 = int1 // 100
    n3 = int2 % 100
    print('Three 2-digit numbers are :', n1, n2, n3)
    