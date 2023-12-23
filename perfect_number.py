n = int(input("Enter number :"))
summ = 0
for i in range(1, n):
    if (n % i == 0):
        summ = summ + i
if (summ == n):
    print("The number", n, "is a Perfect number!")
else:
    print("The number", n, "is not a Perfect number!")