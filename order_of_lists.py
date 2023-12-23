list1 = ['a', 'b', 'c']
list2 = ['h', 'i', 't']
list3 = ['0', '1', '2']
print("Originally :")
print("List 1 :", list1)
print("List 2 :", list2)
print("List 3 :", list3)

list3.extend(list1)

list3.extend(list2)
print("After adding elements of two lists individually, list now is :")
print(list3)