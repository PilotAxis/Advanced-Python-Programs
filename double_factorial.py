num = int(input("Enter a number :"))
fac = 1
for a in range(num, 0, -2):
    fac *= a
print(num, "!! is :", fac)