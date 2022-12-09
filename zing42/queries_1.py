import connection as con
import pandas as pd


zing = pd.DataFrame(con.zing)
zing.columns=['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP', 'TOTALTRADES', 'ISIN', 'FIELD14',  'NAME_OF_COMPANY','DATE_OF_LISTING', 'PAID_UP_VALUE', 'MARKET_LOT', 'ISIN_NUMBER', 'FACE_VALUE']
gain_arr = []
gain = (zing['CLOSE'] - zing['OPEN'])/zing['OPEN']
gain = pd.DataFrame(gain)
final_op = pd.concat([zing,gain],axis=1)
final_op.columns= ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP', 'TOTALTRADES', 'ISIN', 'FIELD14',  'NAME_OF_COMPANY','DATE_OF_LISTING', 'PAID_UP_VALUE', 'MARKET_LOT', 'ISIN_NUMBER', 'FACE_VALUE','GAIN']
final_op = final_op.sort_values("GAIN", ascending=[False])
print(final_op[:26])