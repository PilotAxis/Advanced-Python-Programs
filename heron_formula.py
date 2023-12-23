import math
a, b, c = 17, 23, 30
s = (a+b+c)/2
area = math.sqrt(s * (s-a)*(s-b)*(s-c))
print("Sides of triangle :", a, b, c)
print("Area :", area, "units square")