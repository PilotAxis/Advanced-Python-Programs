lst = eval(input('Enter a list :'))
while True :
    print("Main Menu")
    print("1. Insert")
    print("2. Delete")
    print("3. Exit")
    ch = eval(input("Enter your choice 1/2/3 :"))
    if ch == 1 :
        ins = eval(input("Enter item :"))
        ind = eval(input("Insert at which position?"))
        index = ind - 1
        lst.insert(index, ins)
        print("Success! List now is :", lst)
    elif ch == 2 :
        print("     Deletion Menu     ")
        print("1. Delete using Value")
        print("2. Delete using index")
        print("3. Delete a sublist")
        cs = int(input("Enter choice (1 or 2 or 3) :"))
        if cs == 1:
            de = eval(input("Enter item to be deleted :"))
            lst.remove(de)
            print("List now is :", lst)
        elif cs == 2 :
            dex = eval(input("Enter index of item to be deleted :"))
            lst.pop(dex)
            print("List now is :", lst)
        elif cs == 3:
            lo = eval(input("Enter lower limit of list slice to be deleted :"))
            uo = eval(input('Enter upper limit of list slice to be deleted :'))
            del lst[lo : uo]
            print("List now is :", lst)
        else:
            print("Valid choices are 1/2/3 only.")
    elif ch == 3:
        break;
    else:
        print("Valid choices are 1/2/3 only.")
        
