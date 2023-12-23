num = int(input("Enter a number (0..999) :"))
if num < 0 :
    print("Invalid entry. Valid range is 0 to 999.")
elif num < 10 :
    print("Single digit number is entered")
elif num < 100 :
    print("Two digit number is entered")
elif num <= 999 :
    print("Three digit number is entered")
else :
    print("Invalid entry. Valid range is 0 to 999.")