#%%
import requests
import pandas as pd
import numpy as np


#%%

def tot():
    url = 'https://mops.twse.com.tw/mops/web/t163sb04'
    r = requests.post(url, {
            'encodeURIComponent':1,
            'step':1,
            'firstin':1,
            'off':1,
            'TYPEK':'sii',
            'year':108,
            'season':2,
        })

    r.encoding = 'utf8'

    df=pd.read_html(r.text)[12]
    df.to_csv('f_report_tot.csv',mode='a',encoding='utf-8-sig')
    print(df)
    return

# %%


