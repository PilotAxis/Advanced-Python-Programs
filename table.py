num = int(input('Enter a number :'))
ran = int(input('Define a specific range for the table :'))
for a in range(1, ran):
    print(num, 'x', a, '=', num*a)