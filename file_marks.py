#Writing
myfile = open(r"D:\File Handling Files\Marks.txt", "w")
n = int(input("How many students?"))
for i in range(n):
    roll = int(input("Roll :"))
    name = input("Name :")
    marks = float(input("Marks :"))
    rec = str(roll) + ',' + name + ',' + str(marks) + '\n'
    myfile.write(rec)
myfile.close()


#Displaying
myfile = open(r"D:\File Handling Files\Marks.txt", "r")
con = myfile.read()
print(con)
myfile.close()
