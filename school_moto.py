print("Enter words of your school motto, one by one")
w1 = input('Enter word 1 :')
w2 = input('Enter word 2 :')
w3 = input('Enter word 3 :')
w4 = input('Enter word 4 :')
motto = " ".join([w1, w2, w3, w4])
print("Enter your school\'s foundation date.")
dd = input("Enter dd :")
mm = input("Enter mm :")
yyyy = input('Enter yyyy :')
dt = "/".join([dd, mm, yyyy])
print("School motto :", motto)
print("School foundation date :", dt)