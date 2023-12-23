t = int(input("How many terms?(enter 2+ value) :"))
first = 0
second = 1
print("\nFibonacci series is :")
print(first, ",", second, end=",")

for i in range(2, t):
    next = first + second
    print(next, end=", ")
    first = second
    second = next