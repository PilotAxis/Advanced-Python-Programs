n = 5
s = 0
for i in range(n, 0, -1):
    for j in range(1, s+1):
        print(end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    s+=2
    print()
