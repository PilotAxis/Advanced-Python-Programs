import csv
with open(r"C:\Users\moham\Onedrive\Documents\File Handling\compresult.csv", 'r') as fh :
    creader = csv.reader(fh)
    for rec in creader :
        print(rec)
