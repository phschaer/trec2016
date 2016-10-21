import csv
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x=list()
y=list()

with open('./result.csv', 'r') as csvdata:
    data = csv.reader(csvdata, delimiter=";")
    for row in data:
        qid= row[0]
        tau = row[1]
        x.append(qid)        
        y.append(float(tau))

print y

