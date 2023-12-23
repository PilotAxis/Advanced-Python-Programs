line = input("Enter a line :")
l = u = 0
digit = alpha = sym = 0
for a in line :
    if a.islower():
        l += 1
    elif a.isupper():
        u += 1
    elif a.isdigit():
        digit += 1
    elif a.isalpha():
        alpha += 1
    elif a.isalnum() !=True and a !=' ':
        sym += 1
print("Uppercase :", u)
print("Lowercase :", l)
print("Alphabets :", alpha)
print("Digits :", digit)
print("Symbols :", sym)