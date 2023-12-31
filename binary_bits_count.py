def countBits(N):
    s = input("What do you want to calculate ?(0 or 1) :")
    return bin(N).replace("0b", "").count(s)

n = int(input("Enter number :"))
print(countBits(n))