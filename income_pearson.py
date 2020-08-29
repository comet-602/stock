import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# 讀取檔案
df=pd.read_csv("data/income_clean.csv", encoding = 'utf-8')
print(df.shape)

# 印出pearson結果
df1=df.iloc[:,2::]
print(df1.shape)

df1_corr=df1.corr()
df1_corr.to_csv('data/income_pearson.csv',mode='a',encoding='utf-8-sig',index=0)

print('===============================')

### 去掉高度相關的欄位 ###

# 取得上三角的值
upper = df1_corr.where(np.triu(np.ones(df1_corr.shape), k=1).astype(np.bool))

# 找到corr大於0.9的欄位，並刪除
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
print(to_drop)
df.drop(to_drop, axis=1, inplace=True)

# 增加分類標籤，盈餘正為1，負為0
df['label'] = df["基本每股盈餘（元）"].map(lambda x: 1 if x > 0 else 0)

# 印出整理後的欄位
print(df.shape)
df.to_csv('data/income_after_pearson.csv',mode='a',encoding='utf-8-sig',index=0)


## 繪圖
#plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
#sns.heatmap(df1.corr(method ='pearson'),annot=True)
#sns.pairplot(df1)
#plt.show()
