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
cursor = cnx.cursor(dictionary=True)
x=100
SCSECTORS=[]
NCSECTORS=[]
cursor.execute("select DISTINCT ServingSector from tbmrodata;")
result=cursor.fetchall()
print(len(result))
for i in result:
    SCSECTORS.append(i['ServingSector'])
cursor.execute("select DISTINCT InterferingSector from tbmrodata;")
result=cursor.fetchall()
print(len(result))
for i in result:
    NCSECTORS.append(i['InterferingSector'])
print(SCSECTORS)
print(NCSECTORS)
for i in SCSECTORS:
    for j in NCSECTORS:
        cursor.execute("select LteScRSRP-tbmrodata.LteNcRSRP as C2I from tbmrodata where ServingSector='"+i+"' and InterferingSector='"+j+"';")
        C2IRESULT=cursor.fetchall()
        print(len(C2IRESULT))
        C2I=[]
        if(len(C2IRESULT)>x):
            for k in C2IRESULT:
                C2I.append(int(k['C2I']))
            C2IMEAN=numpy.mean(C2I)
            C2ISTANDARD=numpy.std(C2I)
            PCIC2I9=scipy.stats.norm.cdf(x=9,loc=C2IMEAN,scale=C2ISTANDARD)
            PCIABS6=scipy.stats.norm.cdf(x=6,loc=C2IMEAN,scale=C2ISTANDARD)-scipy.stats.norm.cdf(x=-6,loc=C2IMEAN,scale=C2ISTANDARD)
            print("insert into tbc2i values('"+i+"','"+j+"',"+str(C2IMEAN)+","+str(C2ISTANDARD)+","+str(PCIC2I9)+","+str(PCIABS6)+");")
            cursor.execute("insert into tbc2i values('"+i+"','"+j+"',"+str(C2IMEAN)+","+str(C2ISTANDARD)+","+str(PCIC2I9)+","+str(PCIABS6)+");")
            cnx.commit()