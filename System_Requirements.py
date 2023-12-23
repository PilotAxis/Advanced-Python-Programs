def cpu_gen():
    print("Question 1 :")
    print("Hint : 8, 9 etc.")
    cpu_g = int(input("Enter your CPU Generation :"))
    if cpu_g >= 8:
        print("OK, Compatible!")
        ram_check()
    elif cpu_g == 7:
        print("Hmm, Only some series of 7th Gen are compatible!")
        print("YOU ARE GOOD TO GO TILL NOW!")
        return cpu_series_7()
    elif cpu_g <= 6:
        print("Sorry!, Not Compatible.")
        exit()
    else:
        print("INVALID!")
        exit()

def cpu_series_7():
    print("Hint : Tell Answer as i3, i5, i7, i9")
    series = input("Your CPU Series :")
    if series == "i3":
        print("Sorry!, Not Compatible.")
        exit()
    elif series == "i5":
        print("Sorry!, Not Compatible.")
        exit()
    elif series == "i7":
        print("Sorry!, Not Compatible.")
        exit()
    elif series == "i9":
        print("Great, Compatible!")
        ram_check()
    else:
        print("INVALID!")
        exit()
def ram_check():
    print("Tell only in Numbers...")
    ram = int(input("Enter the amount of RAM :"))
    if ram < 4:
        print("Sorry!, Not Possible.")
        exit()
    elif ram >= 4 :
        print("Good to GO!")
        Secure()
    else:
        print("INVALID!")
        exit()

def Secure():
    print("Only YES/NO in Answer.")
    secure_boot = input("Do you have Secure Boot ?")
    if secure_boot == 'YES':
        print("Very Good!")
        tpm_check()
    elif secure_boot == 'NO':
        print("Sorry, Not Possible!")
        exit()
    else:
        print("Invalid!")
        exit()

def tpm_check():
    print("Only YES/NO in Answer.")
    tpm = input("Do you have TPM 2.0 ?")
    if tpm == 'YES':
        print("Very Good!")
        Clear()
    elif tpm == 'NO':
        print("Sorry, Not Possible!")
        exit()
    else:
        print("Invalid!")
        exit()

def Clear():
    print("Now, You have passed all the assessments!")
    print("Your PC is Now Compatible with Windows 11.")
    print("Thanks for using the program!")

def exit():
    print("Sorry, Your PC cannot run Windows 11")
    print("Continue running your current OS!")
    print("Thanks...")



# __main__
print("Program to tell if your System is Compatible with Windows 11")
print("Some Questions will be asked to you...")
print("Tell Your Laptop Brand?")
brand = input("Answer :")
print('OK')
cpu_gen()



