import pickle
emp = {}
empfile = open(r"C:\Users\moham\Onedrive\Documents\File Handling\Emp.dat", 'rb')
try :
    while True :
        emp = pickle.load(empfile)
        print(emp)
except EOFError :
    empfile.close()
