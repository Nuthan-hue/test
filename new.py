import pymongo
import csv
from collections import Counter
import pandas as pd
c=pymongo.MongoClient('localhost',27017)
# c=pymongo.MongoClient('host.docker.internal',27017)
db=c['mydb']
collection=db['data']
def fun(filename):
    with open(filename) as file:
        f= pd.csv_reader   (file)
        print(f)
        a=[]
        for row in f:
            a.append(row['responce_code'])
    c=dict(Counter(a))
    thres=c.keys()
    a=['1011','1110','1001','1010','1101','1100','1000']
    for i in a:
        if i in thres:
            prit("nothing")
            pass
        else:
            c[i]=0
    ok=c['1011']+c['1110']+c['1001']+c['1010']
    actual=ok+c['1101']+c['1100']+c['1000']
    theshold=(ok/actual)*100
    print(theshold)
def c(filename):
    with open(filename) as file:
        file_data=csv.DictReader(file)
        x=collection.insert_many(file_data)

def f(filename):
    with open(filename) as file:
        f=pd.read_csv(file)
        a=0
        b=0
        for row in f:
            if (row['interface']==LINK and row['branch']==LTS):
                if (row['responce_code']=='001' or row['responce_code']=='001'):
                    a=a+1
                else:
                    b=b+1
        print(a,b)
c('original1.csv')

f('original1.csv')
