N = int(input())
lst = []
for i in range(1, N+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
print(lst)