import requests
import pandas as pd
import numpy as np

df=pd.read_csv("income_sheet.csv", encoding = 'cp950')
print(df.info())
df_f=df.iloc[:,0:3]
df_b=df.iloc[:,4::]
# print(df_f.shape)
# print(df_b.shape)

# 將缺失值替換為0
for i in df_b.columns:
    if df_b[i].dtypes == 'int64' or df_b[i].dtypes == 'float64':
        #print('a:',i,df_b[i].dtypes)
        df_b[i]=df_b[i].replace('--','0')
    else:
        #print('b:',i,df_b[i].dtypes)
        df_b[i]=df_b[i].str.replace('--','0')
df_b=df_b.iloc[:,3::].astype(float)

df=

print(df.info())
df.to_csv('income_clean.csv',encoding='utf-8-sig',index=0)
