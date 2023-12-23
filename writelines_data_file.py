fileout = open(r"C:\Users\moham\OneDrive\Documents\File Handling\Student3.txt", 'w')
list1 = []
for i in range(5) :
    name = input("Enter name of the student :")
    list1.append(name + '\n')
fileout.writelines(list1)
fileout.close()
