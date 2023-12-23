lst1 = eval(input("Enter list 1 :"))
lst2 = eval(input("Enter list 2 :"))
m1 = max(lst1)
m2 = max(lst2)
if m1 >= m2 :
    print(m1, "the maximum value is in list 1 at index", lst1.index(m1))
else:
    print(m2, "the maximum value is in list 2 at index", lst2.index(m2))
