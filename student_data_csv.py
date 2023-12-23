import csv
fh = open(r"C:\Users\moham\Onedrive\Documents\File Handling\Student.csv", "w")
stuwriter = csv.writer(fh) #delimiter = '|', by default taken as ',' 
stuwriter.writerow(['Rollno', 'Name', 'Marks'])

for i in range(2):
    print("Student record", (i+1))
    rollno = int(input("Enter rollno :"))
    name = input("Enter name :")
    marks = float(input("Enter marks :"))
    sturec = [rollno, name, marks]
    stuwriter.writerow(sturec)
fh.close()
