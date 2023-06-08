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
data=pandas.read_csv("tbCell.csv",skiprows=index,nrows=step,header=0,encoding='GBK')
while not data.empty:
    data.dropna(axis=0,inplace=True)
    try:
        for rowindex,iter in data.iterrows():
            cursor.execute("insert into tbcell values ('" + str(iter[0]) + "','" + str(iter[1]) + "','" + str(iter[2]) + "'," + str(
        iter[3]) + ",'" + str(iter[4]) + "'," + str(iter[5]) + "," + str(iter[6]) + "," + str(iter[7]) + "," + str(
        iter[8]) + "," + str(iter[9]) + "," + str(iter[14]) + "," + str(iter[15]) + "," + str(iter[16]) + "," + str(
        iter[17]) + "," + str(iter[18]) + ") ON DUPLICATE KEY UPDATE CITY=VALUES(CITY),SECTOR_NAME=VALUES(SECTOR_NAME),ENODEB_ID=VALUES(ENODEB_ID),ENODEB_NAME=VALUES(ENODEB_NAME),EARFCN=VALUES(EARFCN),PCI=VALUES(PCI),PSS=VALUES(PSS),SSS=VALUES(SSS),TAC=VALUES(TAC),AZIMUTH=VALUES(AZIMUTH),HEIGHT=VALUES(HEIGHT),ELECTTILT=VALUES(ELECTTILT),MECHTILT=VALUES(MECHTILT),TOTLETILT=VALUES(TOTLETILT);")
            cnx.commit()
    except mysql.connector.errors.ProgrammingError:
        a=0
    index+=step
    try:
        data = pandas.read_csv("tbCell.csv", skiprows=index, header=None,nrows=step, encoding='GBK')
    except pandas.errors.EmptyDataError:
        data=pandas.DataFrame(data=None)