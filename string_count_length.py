str = input("Enter a string :")
st = str.split(' ')
for word in st :
    print(word, " (", len(word), ")")