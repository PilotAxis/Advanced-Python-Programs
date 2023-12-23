radius = float(input("Enter radius of the circle :"))
print("1. Calculate Area")
print("2. Calculate Perimeter")
choice = int(input('Enter your choice (1 or 2) :'))
if choice == 1 :
    area = 3.14159*radius*radius
    print('Area of circle with radius', radius, 'is', area)
else:
    perm = 2*3.14159*radius
    print('Perimeter of circle with radius', radius, 'is', perm)