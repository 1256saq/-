import pandas
import xml.sax
import numpy
from sqlalchemy import create_engine
import mysql.connector
import scipy.stats

USER='root'
PASSWORD='!Asd5193371'
HOST='127.0.0.1'
PORT=3306
db='dbas'
engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=GBK'
                           % (USER, PASSWORD, HOST, PORT, db))
data=pandas.read_sql("select * from tbcell",engine)
print(data)
data.to_csv("tbcelloutput.csv",header=True,encoding="utf_8_sig")