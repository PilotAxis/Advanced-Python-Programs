num = int(input("Enter an Integer (>1000) :"))
tnum = num
reverse = 0
while tnum :
    digit = tnum%10
    tnum = int(tnum/10)
    reverse = reverse * 10 + digit
print('Reverse of', num, 'is', reverse)