import pandas
csv=pandas.read_csv('tbCell.csv',encoding='GBK',usecols=['SECTOR_ID','LONGITUDE','LATITUDE'])
dict={}
for index, row in csv.iterrows():
    dict[row['SECTOR_ID']]=[row['LONGITUDE'],row['LATITUDE']]
with open('coordinate.txt','a+',encoding='utf-8') as f:
    f.write(str(dict))