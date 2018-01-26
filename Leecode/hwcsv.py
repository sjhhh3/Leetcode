import csv

with open('hw_data.csv') as data:
    readdata = csv.reader(data, delimiter=',')

    weightlist = []
    for row in readdata:
        print(row)
        weight = row[2]
        weightlist.append(weight)

    aveweight = sum(weightlist[1:])/(len(weightlist)-1)
    print(aveweight)