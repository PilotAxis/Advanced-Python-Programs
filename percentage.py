total = 0
for i in range(5):
    marks = float(input("Enter marks in subject " + str(i+1) +" : "))
    total += marks
perc = total / 5
if perc >= 81 :
    grade = 'A'
elif perc >= 69 :
    grade = 'B'
elif perc >= 50:
    grade = 'C'
elif perc >= 33:
    grade = 'D'
else:
    grade = "E"
print("Total Marks :", total, "\t Percentage :", perc)
print("\t\t\t Grade :", grade)
    
