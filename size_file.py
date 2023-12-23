myfile = open(r"C:\Users\moham\OneDrive\Documents\File Handling\poem.txt", 'r')
str1 = " "
size = 0
tsize = 0
while str1 :
    str1 = myfile.readline()
    tsize = tsize + len(str1)
    size = size + len(str1.strip())
print("Size of the file after removing all EOL characters & blank line :", size)
print("The Total size of the file :", tsize)
myfile.close()
