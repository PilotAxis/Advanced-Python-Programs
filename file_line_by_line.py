myfile = open(r"C:\Users\moham\OneDrive\Documents\File Handling\poem.txt", 'r')
str = " "
while str:
    str = myfile.readline()
    print(str, end='')
myfile.close()
