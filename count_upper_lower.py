str1 = input("Enter a string :")
ucase, lcase = 0, 0
for ch in str1:
    if ch >= 'A' and ch <= 'Z':
        ucase += 1
    if ch >= 'a' and ch <= 'z':
        lcase += 1
print("No. of uppercase letters :", ucase)
print("No. of lowercase letters :", lcase)