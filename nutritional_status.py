weight = float(input("Enter weight in kg :"))
height = float(input("Enter height in m :"))
bmi = weight/(height**2)
print("BMI is :", bmi, end=" ")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")