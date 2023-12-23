import random
n = int(input("How many dice throws ?"))
for i in range(1, n + 1):
    print("Throw", i, ":", random.randint(1, 6))