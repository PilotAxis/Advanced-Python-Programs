ch = input('Enter a single character :')
if ch >= 'A' and ch <= 'Z' :
    print('You entered a UPPERCASED letter.')
elif ch >= 'a' and ch <= 'z' :
    print('You entered a lowercased letter.')

elif ch >= '0' and ch <= '9' :
    print('You entered a digit.')

else:
    print('You entered a special character.')