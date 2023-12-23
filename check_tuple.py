tup = eval(input("Enter tuple :"))
ln = len(tup)
num = tup.count(tup[0])
if num == ln :
    print("Tuple contains all the same elements.")
else:
    print("Tuple contains different elements.")
