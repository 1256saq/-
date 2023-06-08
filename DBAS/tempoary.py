# import pandas
# import xml.sax
# import mysql.connector
# cnx = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password="!Asd5193371",
#     port=3306,
#     db='dbas',
#     charset='utf8'
# )
# cursor = cnx.cursor()
# sql="select * from tbmrodata"
# data=pandas.read_sql(sql,cnx,params=[])
import numpy
import scipy.stats

list=[-1,-2,-3,-4,5]
MEAN = numpy.mean(list)
STANDARD = numpy.std(list)
MEAN=0
STANDARD=1
PCIABS6 = scipy.stats.norm.cdf(x=1, loc=MEAN, scale=STANDARD)
print(PCIABS6)