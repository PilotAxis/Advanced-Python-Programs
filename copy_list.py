lst = eval(input("Enter a list :"))
lsrt = lst.copy()
print("Original list :", lst)
print("Created copy of the list :", lsrt)
lsrt[0] += 10
lsrt[-1] += 10
print("Copy of the list after changes :", lsrt)
print("Original list :", lst)