
import requests
from io import StringIO
import pandas as pd
import numpy as np
import datetime
import time

import stock_id


def crawl_three(date):
    r = requests.get('https://www.twse.com.tw/fund/T86?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&selectType=ALL')
    try:
        df = pd.read_csv(StringIO(r.text))

        df[df['證券代號'].isin(stock_id.id())]
        print(df)
        #ret.to_csv('stock_three_test.csv',mode='a',encoding='utf-8-sig', header=0)
        return ret
    except:
        pass
        return 'no'

data = {}
n_days = 1
#date = datetime.datetime.now()

date0 = '2020-08-07 09:01:01.403545'
date = datetime.datetime.strptime(date0,'%Y-%m-%d %H:%M:%S.%f')

data[date.date()] = crawl_three(date)
