import requests
import pandas as pd
import numpy as np

df=pd.read_csv("income_sheet.csv", encoding = 'cp950')
print(df.info())
for i in df.columns:
    if df[i].dtypes == 'int64' or df[i].dtypes == 'float64':
        #print('a:',i,df[i].dtypes)
        df[i]=df[i].replace('--','0')
    else:
        #print('b:',i,df[i].dtypes)
        df[i]=df[i].str.replace('--','0')
df=df.iloc[:,3::].astype(float)
print(df.info())
df.to_csv('income_clean.csv',encoding='utf-8-sig',index=0)