lst = eval(input('Enter tuple :'))
length = len(lst)
mean = sum = 0
for i in range(0, length):
    sum += lst[i]
mean = sum / length
print("Given tuple is :", lst)
print("The mean of the given list is :", mean)