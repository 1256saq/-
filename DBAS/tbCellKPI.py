import pandas
import mysql.connector
cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password="!Asd5193371",
    port=3306,
    db='dbas',
    charset='utf8'
)
cursor = cnx.cursor()
step=1000
index=0
data=pandas.read_csv("tbCellKPI.csv",skiprows=index,nrows=step,header=0,encoding='utf-8')
while not data.empty:
    print(data)
    data.dropna(axis=0,inplace=True)
    try:
        for rowindex,iter in data.iterrows():
            cursor.execute("insert into tbcellkpi values ('" + str(iter[0]) + "','" + str(iter[1]) + "','" + str(iter[2]) + "','" + str(
        iter[3]) + "'," + str(iter[4]) + "," + str(iter[5]) + "," + str(iter[6]) + ") ON DUPLICATE KEY UPDATE StartTime=VALUES(StartTime),ENODEB_NAME=VALUES(ENODEB_NAME),SECTOR_DESCRIPTION=VALUES(SECTOR_DESCRIPTION),ENODEB_NAME=VALUES(ENODEB_NAME),RCCConnSUCC=VALUES(RCCConnSUCC),RCCConnATT=VALUES(RCCConnATT),RCCConnRATE=VALUES(RCCConnRATE);")
            cnx.commit()
    except mysql.connector.errors.ProgrammingError:
        a=0
    index+=step
    try:
        data = pandas.read_csv("tbCellKPI.csv", skiprows=index, header=None,nrows=step, encoding='utf-8')
    except pandas.errors.EmptyDataError:
        data=pandas.DataFrame(data=None)