import math
length = float(input('Enter length of the ladder :'))
angle = float(input('Enter angle of leaning (in degrees) :'))
ang_radian = math.radians(angle)
height = length*math.sin(ang_radian)
print("Ladder's height on the wall :", height)