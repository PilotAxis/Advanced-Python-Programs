tup = eval(input('Enter a tuple :'))
if sorted(tup, reverse = True) == list(tup):
    print('Tuple is sorted in descending order.')
else:
    print("Tuple is not sorted in descending order.")