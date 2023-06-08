import pandas
import xml.sax
import numpy
import mysql.connector
import scipy.stats
cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password="!Asd5193371",
    port=3306,
    db='dbas',
    charset='utf8'
)
ResultSet=set()
cursor = cnx.cursor(dictionary=True)
x=0.4
collar={}
SS=[]
cursor.execute("select DISTINCT SCELL from tbc2i;")
result=cursor.fetchall()
print(len(result))
for i in result:
    SS.append(i['SCELL'])
for j in SS:
    collar[j]=[]
    cursor.execute("select NCELL from tbc2i where SCELL='"+j+"' and PCIABS6>"+str(x)+";")
    NR=cursor.fetchall()
    for k in NR:
        collar[j].append(k['NCELL'])
for m in collar.keys():
    for n in collar[m]:
        if (n in collar.keys()):
            for o in collar[n]:
                if(o!=m):
                    ResultSet.add(tuple({m, n, o}))
print(ResultSet)