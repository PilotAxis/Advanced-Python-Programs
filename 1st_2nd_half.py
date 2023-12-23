lst = eval(input("Enter a list :"))
l = len(lst)
mx = max(lst)
ind = lst.index(mx)
if ind <= (l/2):
    print("The maximum element", mx, "lies in the 1st half.")
else:
    print("The maximum element", mx, "lies in the 2nd half.")
