#need to write changes before "continue"
import csv
from check import check_chapter 

def next_check(db):
    # Read the CSV file into a list of lists
    with open(db, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    print(data)
    # Now data is a list of lists, where each inner list is a row of the CSV file.
    # You can modify it as needed. For example, to change the first column of the first row:
    for i in range(len(data)):   
        gno=data[i][1]
        cno=data[i][2]
        dno=data[i][3] 
        if(data[i][3]=='5'):
            data[i][3]='0'
            data[i][2]='0'+str(int(data[i][2])+1)
            if(check_chapter(data[i])):
                continue
            data[i][1]=gno
            data[i][2]=cno
            data[i][3]=dno
        else:
            data[i][3]='5'
            if(check_chapter(data[i])):
                continue
            data[i][3]='0'
            data[i][2]='0'+str(int(data[i][2])+1)
            if(check_chapter(data[i])):
                continue
            data[i][2]='0001'
            data[i][1]=str(int(data[i][1])+1)
            if(check_chapter(data[i])):
                continue
        data[i][1]=gno
        data[i][2]=cno
        data[i][3]=dno
    with open(db, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)