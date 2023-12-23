print('Enter five numbers below')
num1 = float(input('Enter a number :'))
num2 = float(input('Enter a number :'))
num3 = float(input('Enter a number :'))
num4 = float(input('Enter a number :'))
num5 = float(input('Enter a number :'))
divisor = float(input("Enter divisor number :"))
count = 0
print('Multiples of', divisor, 'are :')
remainder = num1%divisor
if remainder == 0 :
    print(num1, sep='')
    count += 1
remainder = num2%divisor
if remainder == 0 :
    print(num2, sep='')
    count += 1
remainder = num3%divisor
if remainder == 0 :
    print(num3, sep='')
    count += 1
remainder = num4%divisor
if remainder == 0 :
    print(num4, sep='')
    count += 1
remainder = num5%divisor
if remainder == 0 :
    print(num5, sep='')
    count += 1
print()
print(count, 'multiples of', divisor, 'found')