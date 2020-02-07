import sqlite3
import pandas as pd
coin = 'BTC'
base = 'USDT'

pair = f'{coin}/{base}'
time_frame = '1h'
symbol = f'{pair}_{time_frame}'

conn = sqlite3.connect('ohlcv.db')
c = conn.cursor()


selection = """SELECT * FROM '%s' """ %(symbol)
df = pd.read_sql(selection, conn)
write = df.to_csv(f'Data\{coin}-{base}_{time_frame}.csv', header=True)
