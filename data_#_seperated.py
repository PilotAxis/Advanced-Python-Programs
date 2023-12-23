myfile = open(r"C:\Users\moham\OneDrive\Documents\File Handling\Answer.txt", 'r')
line = " "
while line :
    line = myfile.readline()
    for word in line.split():
        print(word, end= '#')
    print()
myfile.close()
