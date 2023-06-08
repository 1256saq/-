import pandas
csv=pandas.read_csv('tbC2I.csv',encoding='utf-8',usecols=['SCELL','NCELL','C2I_Mean'])
with open('tbC2I.txt','a+',encoding='utf-8') as f:
    for index,row in csv.iterrows():
        f.write(row['SCELL']+" "+row['NCELL']+" "+str(row['C2I_Mean'])+'\n')