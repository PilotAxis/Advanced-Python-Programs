import csv
fh = open(r"C:\Users\moham\Onedrive\Documents\File Handling\compresult.csv", 'w')
cwriter = csv.writer(fh)
compdata = [
    ['Name', 'Points', 'Rank'],
    ['Ahmed', 4500, 23],
    ['Shaad', 4800, 31]]
cwriter.writerows(compdata)
fh.close()
