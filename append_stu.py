import pickle
stu = {}
stufile = open(r"C:\Users\moham\Onedrive\Documents\File Handling\Stu.dat", 'ab')
ans = 'y'
while ans == 'y' :
    rno = int(input("Enter roll number :"))
    name = input("Enter name :")
    marks = float(input("Enter marks :"))
    stu['Rollno'] = rno
    stu['Name'] = name
    stu['Marks'] = marks
    pickle.dump(stu, stufile)
    ans = input("Want to append more records? (y/n)...")
stufile.close()
