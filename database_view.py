import sqlite3
import pandas as pd
import calendar
import time

pair = 'CMT/BNB'
time_frame = '1h'
symbol = f'{pair}-{time_frame}'


conn = sqlite3.connect('ohlcv.db')
c = conn.cursor()


selection = """SELECT * FROM '%s'""" %(symbol)
df = pd.read_sql(selection, conn)
#df['EMA10'] = df['Close_'].rolling(window=10).mean()
#df['EMA30'] = df['Close_'].rolling(window=30).mean()
#write = df.to_csv(f'Data\{symbol}.csv', header=True)
print(df)