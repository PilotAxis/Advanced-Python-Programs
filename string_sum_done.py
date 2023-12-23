total = 0
s = input("Enter a number or 'done' :")
while s != 'done' :
    num = int(s)
    total += num
    s = input("Enter a number or 'done' :")
print("The sum of entered numbers is", total)
