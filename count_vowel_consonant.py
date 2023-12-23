myfile = open(r"C:\Users\moham\OneDrive\Documents\File Handling\Answer.txt", 'r')
ch = " "
vcount = 0
ccount = 0
while ch :
    ch = myfile.read(1)
    if ch in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'] :
        vcount += 1
    else :
        ccount += 1
print("Vowels in the file :", vcount)
print("Consonants in the file :", ccount)
myfile.close()
