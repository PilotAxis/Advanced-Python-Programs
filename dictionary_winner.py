n = int(input("How many students ?"))
compwinners = {}
for a in range(n):
    key = input("Name of the student :")
    value = int(input("Number of competitions won :"))
    compwinners[key] = value
print("The dictionary now is :")
print(compwinners)