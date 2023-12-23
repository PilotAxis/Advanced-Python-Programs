num = int(input("Enter a number (0..999) :"))
if num < 0 or num > 999 :
    print("Invalid entry. Valid range is 0 to 999.")
else :
    if num < 10 :
        print("Single digit number is entered")
    else :
        if num < 100 :
            print("Two digit number is entered")
        else :
            print("Three digit number is entered")