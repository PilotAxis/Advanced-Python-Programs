import pickle
stu = {}
found = False
fin = open(r"C:\Users\moham\Onedrive\Documents\File Handling\Stu.dat", 'rb+')

try :
    while True :
        rpos = fin.tell()
        stu = pickle.load(fin)

        if stu['Marks'] > 81 :
            stu['Marks'] += 2
            fin.seek(rpos)
            pickle.dump(stu, fin)

            found = True
except EOFError :
    if found == False:
        print("No record(s) Found")
    else:
        print("Successfully updated record(s)")
    fin.close()
        
