info = {'Riya' : 'CSc', 'Mark' : 'Eco', 'Ishpreet' : 'Eng', 'Kamaal' : 'Env.Sc'}
inp = input("Enter value to be searched for :")
if inp in info.values():
    for a in info:
        if info[a] == inp : #using .upper() in the if statement ignores the case sensitivity while typing the values.
            print("The key of given value is", a)
            break
    else:
        print("Given value does not exist in dictionary")
