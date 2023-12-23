s = input("Enter a string :")
dsum = 0
for a in s :
    if a.isdigit():
        dsum += int(a)
print("Sum of string's digits is :", dsum)