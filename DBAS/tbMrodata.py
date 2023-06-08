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
step=10000
index=0
data=pandas.read_csv("tbMROData.csv",skiprows=index,nrows=step,header=0,encoding='utf-8')
while not data.empty:
    print(data)
    data.dropna(axis=0,inplace=True)
    try:
        for rowindex,iter in data.iterrows():
            cursor.execute("insert into tbmrodata values ('" + str(iter[0]) + "','" + str(iter[1]) + "','" + str(iter[2]) + "','" + str(
        iter[3]) + "'," + str(iter[4]) + "," + str(iter[5]) + "," + str(iter[6]) + ") ON DUPLICATE KEY UPDATE TimeStamp=VALUES(TimeStamp),ServingSector=VALUES(ServingSector),InterferingSector=VALUES(InterferingSector),LteScRSRP=VALUES(LteScRSRP),LteNcRSRP=VALUES(LteNcRSRP),LteNcEarfcn=VALUES(LteNcEarfcn),LteNcPci=VALUES(LteNcPci);")
            cnx.commit()
    except mysql.connector.errors.ProgrammingError:
        a=0
    index+=step
    try:
        data = pandas.read_csv("tbMROData.csv", skiprows=index, header=None,nrows=step, encoding='utf-8')
    except pandas.errors.EmptyDataError:
        data=pandas.DataFrame(data=None)