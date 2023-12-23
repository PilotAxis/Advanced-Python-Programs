n = int(input("How many students?"))
stu = {}
for i in range(1, n+1):
	print("Enter details of student", (i))
	rollno = int(input("Roll number :"))
	name = input("Name :")
	marks = float(input("Marks :"))
	d = {"Roll_no : rollno, "Name" : name,     \"Marks" : marks}
	key = "Stu" + str(i)
	stu[key] = d
print(" Students with marks > 75 are:")
for i in range(1, n+1):
	key = "Stu" + str(i)
	if stu[key]["Marks"] >= 75 :
		print(stu[key])