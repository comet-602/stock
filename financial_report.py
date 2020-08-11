#%%
import requests
import pandas as pd
import numpy as np

# 爬取目標網站
year = 107
season = 4
stock_number = 1101

ProfitAndLoseURL = "https://mops.twse.com.tw/mops/web/ajax_t164sb04";    # 損益表
CashFlowStatementURL = "http://mops.twse.com.tw/mops/web/ajax_t164sb05"; # 資產負債表

def crawl_financial_Report(url):
    
    form_data = {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'co_id':stock_number,
        'year': year,
        'season': season,
    }

    r = requests.post(url,form_data)
    html_df = pd.read_html(r.text)[1].fillna("")
    html_df.to_csv('financial_report.csv',mode='a',encoding='utf-8-sig')
    return html_df
#%%
crawl_financial_Report(ProfitAndLoseURL)


# %%
