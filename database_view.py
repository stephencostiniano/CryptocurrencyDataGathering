import sqlite3
import pandas as pd

pair = 'ETH/USDT'
time_frame = '1h'
symbol = f'{pair}_{time_frame}'

conn = sqlite3.connect('ohlcv.db')
c = conn.cursor()


selection = """SELECT * FROM '%s' """ %(symbol)
df = pd.read_sql(selection, conn)
print(df)