fileout = open(r"C:\Users\moham\OneDrive\Documents\File Handling\Student1.txt", 'w')
for i in range(5):
    name = input("Enter name of the student :")
    fileout.write(name)
    fileout.write('\n')
fileout.close()
