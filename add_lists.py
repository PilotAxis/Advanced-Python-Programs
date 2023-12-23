lst1 = ['a', 'b', 'c']
lst2 = ['h', 'i', 't']
lst3 = ['0', '1', '2']
print("Originally :")
print("List 1 :", lst1)
print("List 2 :", lst2)
print("List 3 :", lst3)
lst1.append(lst2)
lst1.insert(0, lst3)
print("After adding two lists as individual elements, list now is :")
print(lst1)