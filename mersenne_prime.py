for a in range(1, 21):
    mersum = 2 ** a -1
    mid = int(mersum/2) + 1
    for b in range(2, mid):
        if mersum % b == 0:
            print(mersum)
            break
    else:
        print(mersum, "\tPrime")