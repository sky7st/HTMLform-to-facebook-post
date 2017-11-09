import csv,os
chdir = os.getcwd() 
with open(chdir+'/response/test.csv','r') as fin:
    reader=csv.reader(fin)
    for row in reader:
        for items in row:
            print(items.encode('utf-8'))