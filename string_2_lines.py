import pickle
string = "This is my first line. This is second line."

with open(r"C:\Users\moham\Onedrive\Documents\File Handling\myfile.info", 'wb') as fh :
    pickle.dump(string, fh)

print("File successfully created.")
