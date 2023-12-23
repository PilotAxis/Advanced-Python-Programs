"""import pickle
stu = {}
found = False
stufile = open(r"D:\File Handling Files\Stu.dat", "rb+")
try :
    while True :
        rpos = stufile.tell()
        stu = pickle.load(stufile)
        if stu['Marks'] > 81 :
            stu['Marks'] += 2
            stufile.seek(rpos)
            pickle.dump(stu, stufile)
            found = True
except EOFError:
    if found == False:
        print("No Record")
    else:
        print("Success!")"""

import pickle
stu = {}
stufile = open(r"D:\File Handling Files\Stu.dat", "rb")
try :
    while True:
        stu = pickle.load(stufile)
        print(stu)
except EOFError:
    stufile.close()
