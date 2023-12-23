alst = [15, 6, 13, 22, 3, 52, 2]
print('Original list is :', alst)
n = len(alst)
for i in range(n):
    for j in range(0, n-i-1):
        if alst[j] > alst[j+1]:
            alst[j], alst[j+1] = alst[j+1], alst[j]
print("List after sorting :", alst)

