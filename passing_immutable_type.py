def mynum(a):
    print("Second Case :", a)
    a += 1
    print("Third Case :", a)
    #using return will not change value at the end as int is in mutable type.
#__main__
num = 3
print("First Case :", 3)
mynum(num)
print("Fourth Case :", num)
