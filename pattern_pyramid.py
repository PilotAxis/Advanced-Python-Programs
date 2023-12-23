n = 5
s = n * 2 - 1
for i in range(1, n+1):
    for j in range(0, s):
        print(end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    s = s - 2
    print()
