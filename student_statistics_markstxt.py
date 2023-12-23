count = int(input("How many students ?"))
fileout = open(r"C:\Users\moham\OneDrive\Documents\File Handling\Marks.txt", 'w')

for i in range(count):
    print("Enter details of student", (i+1), "below")
    rollno = int(input("Rollno :"))
    name = input("Name :")
    marks = float(input("Marks :"))
    rec = str(rollno) + "," + name + "," + str(marks) + '\n'
    fileout.write(rec)
fileout.close()
