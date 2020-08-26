import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# 讀取檔案
df=pd.read_csv("income_clean.csv", encoding = 'utf-8')
print(df.shape)

# 印出pearson結果
df=df.iloc[:,:]
df1=df.copy()
df1_corr=df1.corr()
df1_corr.to_csv('income_pearson.csv',mode='a',encoding='utf-8-sig',index=0)

print('===============================')

### 去掉高度相關的欄位 ###

# 取得上三角的值
upper = df1_corr.where(np.triu(np.ones(df1_corr.shape), k=1).astype(np.bool))

# 找到corr大於0.9的欄位，並刪除
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
print(to_drop)
df1.drop(to_drop, axis=1, inplace=True)

# 印出整理後的欄位
print(df1.shape)
df1.to_csv('income_after_pearson.csv',mode='a',encoding='utf-8-sig',index=0)


## 繪圖
#plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
#sns.heatmap(df1.corr(method ='pearson'),annot=True)
#sns.pairplot(df1)
#plt.show()
