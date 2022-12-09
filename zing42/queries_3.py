# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:22:45 2022

@author: kavin
"""

import connection as con
import pandas as pd



q = "select a.* , b.open from close_latest a,open_oldest b where a.symbol = b.symbol;"
con.myCursor.execute(q)
monthly = con.myCursor.fetchall()


monthly = pd.DataFrame(monthly)

monthly.columns=['SYMBOL','CLOSE','OPEN']


gain_arr = []

gain = (monthly['CLOSE'] - monthly['OPEN'])/monthly['OPEN']
print(type(monthly['CLOSE'] ))
gain = pd.DataFrame(gain)
final_op = pd.concat([monthly,gain],axis=1)
final_op.columns=['SYMBOL','CLOSE','OPEN','GAIN']

final_op = final_op.sort_values("GAIN", ascending=[False])

print(final_op[:26])
# final_op.columns= ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP', 'TOTALTRADES', 'ISIN', 'FIELD14',  'NAME_OF_COMPANY','DATE_OF_LISTING', 'PAID_UP_VALUE', 'MARKET_LOT', 'ISIN_NUMBER', 'FACE_VALUE','GAIN']
# final_op = final_op.sort_values("GAIN", ascending=[False])
# print(final_op[:26])


