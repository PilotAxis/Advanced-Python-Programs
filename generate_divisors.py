num = int(input('Enter an integer :'))
mid = num / 2
print('The divisors of', num, 'are :')
for a in range(2, mid+1):
    if num%a==0:
        print(a, end='')
    else:
        print('-End-')