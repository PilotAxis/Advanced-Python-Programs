fileout = open(r"C:\Users\moham\OneDrive\Documents\File Handling\Student.dat", 'w')
for i in range(5):
    name = input("Enter name of the student :")
    fileout.write(name)
fileout.close()
