import pickle
stu = {}
found = False
print("Searching in file Stu.dat...")
with open(r"C:\Users\moham\Onedrive\Documents\File Handling\Stu.dat", 'rb') as fin :
    stu = pickle.load(fin)
    if stu['Marks'] > 81 :
        print(stu)
        found = True
if found == False :
    print("NO records with Marks > 81")
else :
    print("Search successful.")
