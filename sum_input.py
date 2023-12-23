n = int(input("Enter limit (n) :"))
ssum = 0
print("1", end=" ")
ssum += 1
for i in range(2, (n + 1)):
    icube = (i*i*i)
    term = 1/icube
    ssum += term
    print("+ 1 /", icube, end=" ")
print("=", ssum)