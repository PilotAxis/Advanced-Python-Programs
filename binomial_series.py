x = int(input("Enter value of x :"))
n = int(input("Enter the power (n) :"))
s = x
sign = +1
for a in range(2, n+1):
    f = 1
    for i in range(1, a+1):
        f *= i
    term = ((x**a)*sign)/f
    s += term
    sign *= -1
print("Sum of first", n, "terms :", s)