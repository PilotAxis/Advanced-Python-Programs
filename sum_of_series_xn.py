x = int(input("Enter value of x :"))
n = int(input("Enter the power(n) :"))
s = 0
sign = +1
for a in range(n + 1):
    term = (x ** a) * sign
    s += term
    sign *= -1
print("Sum of first", n, "terms :", s)