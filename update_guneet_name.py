import pickle
stu = {}
found = False
fin = open(r"C:\Users\moham\Onedrive\Documents\File Handling\Stu.dat", 'rb+')
try :
    while True:
        rpos = fin.tell()
        stu = pickle.load(fin)
        if stu['Name'] == 'Guneet' :
            stu['Name'] = 'Gurnam'
            fin.seek(rpos)
            pickle.dump(stu, fin)
            found = True
except EOFError :
    if found == False:
        print("No Record(s) Found.")
    else:
        print("Record(s) successfully updated.")
    fin.close()
