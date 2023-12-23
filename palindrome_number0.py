num = int(input("Enter number :"))
wnum = num
rev = 0
while (wnum > 0):
    dig = wnum % 10
    rev = rev * 10 + dig
    wnum = wnum//10
if (num == rev):
    print("Number", num, "is an palindrome!")
else:
    print("Number", num, "is not a palindrome!")