import requests
import pandas as pd
import numpy as np

df=pd.read_csv("data/income_sheet.csv", encoding = 'cp950')
print(df.shape)
df_f=df.iloc[:,0:3]
df_b=df.iloc[:,3::]
# print(df_f.shape)
# print(df_b.shape)
#print(df_f.info())
#print(df_b.info())
# 將缺失值替換為0
for i in df_b.columns:
    if df_b[i].dtypes == 'int64' or df_b[i].dtypes == 'float64':
        #print('a:',i,df_b[i].dtypes)
        df_b[i]=df_b[i].replace('--','0')
    else:
        #print('b:',i,df_b[i].dtypes)
        df_b[i]=df_b[i].str.replace('--','0')
df_b = df_b.iloc[:,:].astype(float)

df = pd.concat([df_f, df_b], axis=1, sort=False)
print(df.shape)
#print(df.info())
df.to_csv('data/income_clean.csv',encoding='utf-8-sig',index=0)
