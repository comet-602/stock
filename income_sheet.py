import requests
import pandas as pd
import numpy as np

# 綜合損益表
def tot(year,season):
    url = 'https://mops.twse.com.tw/mops/web/t163sb04'
    r = requests.post(url, {
            'encodeURIComponent':1,
            'step':1,
            'firstin':1,
            'off':1,
            'TYPEK':'sii',
            'year':year,
            'season':season,
        })
    r.encoding = 'utf8'

    df=pd.read_html(r.text)[12]
    df['date']=str(year)+str(season)
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df=df[cols]
    df.to_csv('income_sheet.csv',mode='a',encoding='utf-8-sig', index=0, header=0)
    
    return print('筆數:',len(df['date']))


# 建立欄位名稱
df=pd.DataFrame(columns=['date','公司代號','公司名稱','營業收入','營業成本','原始認列生物資產及農產品之利益（損失)','生物資產當期公允價值減出售成本之變動利益（損失)',
'營業毛利（毛損)','未實現銷貨（損）益','營業毛利（毛損）淨額','營業費用','其他收益及費損淨額','營業利益（損失）','營業外收入及支出','稅前淨利（淨損）','所得稅費用（利益)',
'繼續營業單位本期淨利（淨損）','停業單位損益','合併前非屬共同控制股權損益','本期淨利（淨損）','其他綜合損益（淨額）','合併前非屬共同控制股權綜合損益淨額','本期綜合損益總額',
'淨利（淨損）歸屬於母公司業主','淨利（淨損）歸屬於共同控制下前手權益','淨利（淨損）歸屬於非控制權益','綜合損益總額歸屬於母公司業主','綜合損益總額歸屬於共同控制下前手權益',
'綜合損益總額歸屬於非控制權益','基本每股盈餘(元)'])
df.to_csv('income_sheet.csv',encoding='utf-8-sig',index=0)


# 控制爬取年度與季
for year in range(102,110):
    for season in [1,2,3,4]:
        try:
            print(year,season)
            tot(year,season)
        except Exception as e:
            print('what:',e)
