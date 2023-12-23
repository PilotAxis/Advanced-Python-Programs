# Alternative 1

'''sum1 = sum2 = 0
num1 = int(input('Enter number 1 :'))
num2 = int(input('Enter number 2 :'))
num3 = int(input('Enter number 3 :'))

sum1 = num1+num2+num3

if num1 != num2 and num1 != num3 :
    sum2 += num1
if num2 != num1 and num2 != num3 :
    sum2 += num2
if num3 != num1 and num3 != num2 :
    sum2 += num3

print('Numbers are', num1, num2, num3)
print('Sum of three given numbers is', sum1)
print('Sum of non-duplicate numbers is', sum2)'''

# Alternative 2
'''sum1 = sum2 = 0
num1 = int(input('Enter number 1 :'))
num2 = int(input('Enter number 2 :'))
num3 = int(input('Enter number 3 :'))
sum1 = num1 + num2 + num3

if num1 == num2 :
    if num3 != num1 :
        sum2 += num3

else:
    if num1 == num3:
        sum2 += num2
    else:
        if num2 == num3 :
            sum2 += num1
        else:
            sum2 += num1 + num2 + num3

print('Numbers are', num1, num2, num3)
print('Sum of three given numbers is', sum1)
print('Sum of non-duplicate numbers is', sum2)'''