import os
import xml.dom.minidom
import gzip
import mysql.connector
cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password="!Asd5193371",
    port=3306,
    db='dbas',
    charset='utf8'
)
cursor = cnx.cursor(dictionary=True)
def isMro(s):
    return 'mro' in s
filelist=os.listdir("xmltest")
for i in list(filter(isMro,filelist)):
    # g_file = gzip.GzipFile(file_name)
    # open(f_name, "wb+").write(g_file.read())
    DOMTree = xml.dom.minidom.parse("xmltest/"+i)
    collection = DOMTree.documentElement
    print(DOMTree.documentElement)
    logs = collection.getElementsByTagName('smr')
    print(logs)
    for log in logs:
        MROid=log.getElementsByTagName('eNBid')[0].childNodes[0].data
        LteScRSRP=log.getElementsByTagName('MR.LteScRSRP')[0].childNodes[0].data
        LteNcRSRP=log.getElementsByTagName('MR.LteNcRSRP')[0].childNodes[0].data
        LteScEarfcn=log.getElementsByTagName('MR.LteScEarfcn')[0].childNodes[0].data
        SeverPci=log.getElementsByTagName('MR.LteScPci')[0].childNodes[0].data
        LteNcEarfcn=log.getElementsByTagName('MR.LteNcEarfcn')[0].childNodes[0].data
        InterferPci=log.getElementsByTagName('MR.LteNcPci')[0].childNodes[0].data
        cursor.execute("select SECTOR_ID from tbcell where ENODEB_ID='"+LteScEarfcn+"';")
        ServingSector=''
        for i in cursor:
            ServingSector=i['SECTOR_ID']
        cursor.execute("select SECTOR_ID from tbcell where ENODEB_ID='" + LteNcEarfcn + "';")
        InterferingSector=''
        for i in cursor:
            InterferingSector=i['SECTOR_ID']
        cursor.execute("select DISTINCT EARFCN from tbcell;")
        EARFCNlist=[]
        for i in cursor:
            EARFCNlist.append(i['EARFCN'])
        if(any(LteNcEarfcn ==EARFCN for EARFCN in EARFCNlist) and int(SeverPci)>0 and int(SeverPci)<500 and int(LteNcRSRP)>=0 and int(LteScRSRP)<=97 and int(LteScRSRP>=0) and int(LteNcRSRP)<=97 and InterferingSector!='' and ServingSector!=''):
            cursor.execute("insert into tbmrodata values ('" + str(iter[0]) + "','" + str(iter[1]) + "','" + str(
                iter[2]) + "','" + str(
                iter[3]) + "'," + str(iter[4]) + "," + str(iter[5]) + "," + str(iter[
                                                                                    6]) + ") ON DUPLICATE KEY UPDATE TimeStamp=VALUES(TimeStamp),ServingSector=VALUES(ServingSector),InterferingSector=VALUES(InterferingSector),LteScRSRP=VALUES(LteScRSRP),LteNcRSRP=VALUES(LteNcRSRP),LteNcEarfcn=VALUES(LteNcEarfcn),LteNcPci=VALUES(LteNcPci);")
            cnx.commit()