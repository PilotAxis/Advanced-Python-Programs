import pickle
emp = {}
myfile = open(r"D:\File Handling Files\Emp.dat", "rb")
try :
    while True:
        emp = pickle.load(myfile)
        print(emp)
except EOFError:
    myfile.close()
