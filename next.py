#must automatically update next after checking too at the end

import csv

def checker(filename,number):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        count=0
        for row in reader:
            if row[0] == number:
                if(row[3]==0):
                    next=str(row[1])+str(row[2])+str(row[3]+5)  #for decimal chapters
                    #check(next)
                    next=str(row[1])+str(row[2]+1)+str(row[3])  #for normal chapters
                    #check(next)
                    next=str(row[1]+1)+str("0001")+str(row[3])  #for next group
                    #check(next)

                else:
                    for i in range(1,5):
                        next=str(row[1])+str(row[2])+str(row[3]+i)  #for decimal chapters
                        #check(next)
                    next=str(row[1])+str(row[2]+1)+"00"
                    #check(next)
                    next=str(row[1]+1)+str("0001")+"00"  #for next group
                    #check(next)
                count+=1
                break