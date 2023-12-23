import pickle
emp1 = {'Empno': 1201, 'Name': 'Anushree', 'Age': 25, 'Salary':47000}
emp2 = {'Empno': 1211, 'Name': 'Zoya', 'Age': 30, 'Salary':48000}
emp3 = {'Empno': 1251, 'Name': 'Simarjeet', 'Age': 27, 'Salary':49000}
emp4 = {'Empno': 1266, 'Name': 'Alex', 'Age': 29, 'Salary':50000}

empfile = open(r"C:\Users\moham\OneDrive\Documents\File Handling\Emp.dat", 'wb')

pickle.dump(emp1, empfile)
pickle.dump(emp2, empfile)
pickle.dump(emp3, empfile)
pickle.dump(emp4, empfile)

print("Successfully written four dictionaries")
empfile.close()
