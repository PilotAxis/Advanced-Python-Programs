print("Enter 2 numbers below")
a = int(input("Enter Number 1 :"))
b = int(input("Enter Number 2 :"))
ch = 0
while ch < 5 :
    print('Calculator Menu')
    print('1.ADD')
    print('2.SUBTRACT')
    print('3.MULTIPLY')
    print('4.DIVIDE')
    print('5.EXIT')

    ch = int(input("Enter Choice (1-5):"))
    break


if ch == 1 :
    c = a + b
    print("Sum :", c)
elif ch == 2 :
    c = a - b
    print("Difference :", c)
elif ch == 3 :
    c = a * b
    print("Product :", c)
elif ch == 4 :
    c = a/b
    print('Quotient :', c)
elif ch == 5:
    print('Exited')

    
