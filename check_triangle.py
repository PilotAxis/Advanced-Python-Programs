angle1 = angle2 = angle3 = 0
angle1 = float(input('Enter Angle 1 :'))
angle2 = float(input("Enter Angle 2 :"))
angle3 = float(input('Enter Angle 3 :'))
if (angle1 + angle2 + angle3) == 180:
    print("Angles form a triangle.")
else:
    print("Angles do not form a triangle.")