print("List Operations ->")
print("1. Add Element")
print("2. Remove Element")
print("3. Find Size")
print("4. Sort List")
lst = []
ans = "yes"
while ans == "yes":
    choice = int(input("Select your choice (1,2,3,4) -> "))
    if choice == 1:
        print("If element is string type str, number type int/float, boolean type bool :")
        type_value = input("Type your element type :")
        if type_value == "str":
            value = input("Enter the element :")
            lst.append(value)
            print(lst)
            ans = input("Want to continue (yes) or exit (no) :")
        elif type_value == "int":
            value = int(input("Enter the element :"))
            lst.append(value)
            print(lst)
            ans = input("Want to continue (yes) or exit (no) :")
        elif type_value == "float":
            value = input("Enter the element :")
            lst.append(value)
            print(lst)
            ans = input("Want to continue (yes) or exit (no) :")
        elif type_value == "bool":
            value = bool(input("Enter the element :"))
            lst.append(value)
            print(lst)
            ans = input("Want to continue (yes) or exit (no) :")