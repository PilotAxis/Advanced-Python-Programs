def interest(principal, time = 2, rate = 0.10):
    return principal*rate*time

#__main__
prin = float(input("Enter principal amount :"))
print("Simple interest with default ROI and time values is :")
si1 = interest(prin)
print("Rs.", si1)
roi = float(input("Enter rate of interest (ROI) :"))
time = int(input("Enter time in years :"))
print("Simple interest with your provided ROI and time values is :")
si2 = interest(prin, time, roi/100)
print("Rs.", si2)