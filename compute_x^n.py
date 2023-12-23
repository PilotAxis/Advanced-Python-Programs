x = int(input("Enter a positive number(x) :"))
n = int(input("Enter the power(n) :"))
power = 1
for a in range(n):
    power = power*x
print(x, "to the power", n, "is", power)