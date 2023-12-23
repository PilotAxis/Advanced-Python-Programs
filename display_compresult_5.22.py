import csv
with open(r"C:\Users\moham\Onedrive\Documents\File Handling\compresult.csv", 'r', newline = '\r\n') as fh :
    creader = csv.reader(fh)
    for rec in creader :
        print(rec)
