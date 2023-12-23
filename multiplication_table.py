for row in range(1, 11) :
    for col in range(1, 11) :
        prod = row*col
        if prod < 10 :
            print('', prod, ' ', end=' ')
        else :
            print(prod, ' ', end=' ')
    print()
