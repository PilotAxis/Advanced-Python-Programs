mylst = list(input("Enter your list :"))
print("Existing list you just created :", mylst)
n = eval(input("Enter the item you want to add in your existing list :"))
if type(n) == type([]):
    mylst.extend(n)
elif type(n) == type(1):
    mylst.append(n)
else:
    print("Only enter a list or an integer.")
print("New list after modifications is :", mylst)