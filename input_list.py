#method 1
'''
lst = map(int, input().split())
print(list(lst))
'''
#method 2

lst = []
n = int(input("Enter how many elements :"))
for i in range(0, n):
    element = int(input())
    lst.append(element)
print(lst)