lst = eval(input("Enter list :"))
l = len(lst)
ch = eval(input("Enter the element to be searched for :"))
for i in range(0, l):
    if ch == lst[i]:
        print(ch, "found at index", i)
        break
else:
    print(ch, "not found in given list")
