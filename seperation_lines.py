s = input("Enter a line of text :")
count = 0
for word in s.split():
    print(word)
    count += 1
print("Total words :", count)