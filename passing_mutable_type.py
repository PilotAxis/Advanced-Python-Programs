def lsty(a):
    print("Second Case :", a)
    a.append(2)
    print("Third Case :", a)
    return #if we don't use return lst will always updates its values and print in the fourth case. Using of return is not necessary.

#__main__
lst = [1]
print("First Case :", lst)
lsty(lst)
print("Fourth Case :", lst)
