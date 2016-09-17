import csv
import random

sheet = csv.reader(open("occupations.csv"))
sheet.next()
jobs = {}


for row in sheet:
    if row[0] != "Total":
        job = row[0]
        percent = float(row[1])
        jobs[job] = percent

#print jobs 

rand = float(random.randrange(998))/10
tracker = rand

print "Random: " + str(rand)


#This is kind of unefficient because the loop doesn't
#stop until the last value no matter what
for key in jobs:
    if tracker != 20000:
        if jobs[key] >= tracker:
            print key 
            tracker = 20000
        else:
            tracker -= jobs[key]




    

