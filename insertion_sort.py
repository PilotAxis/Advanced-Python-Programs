alst = [15, 6, 13, 22, 3, 52, 2]
print('Original list is :', alst)
for i in range(1, len(alst)):
    key = alst[i]
    j = i-1
    while j >= 0 and key < alst[j]:
        alst[j+1] = alst[j]
        j = j-1
    else:
        alst[j+1] = key
print("List after sorting :", alst)