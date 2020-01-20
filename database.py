import sqlite3
import pandas as pd
import time
import datetime
import calendar
import ccxt

exchange = ccxt.binance({'enableRateLimit': True})
pair = 'ETH/USDT'
time_frame = '1h'
symbol = f'{pair}_{time_frame}'

sleep = 2
conn = sqlite3.connect('ohlcv.db')
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS '%s' (Time_ TIMESTAMP, Open_ FLOAT, High_ FLOAT, Low_ FLOAT, Close_ FLOAT, Volume_ FLOAT)" %(symbol))
conn.commit()

start = 0
end = 0
new_time = None
new_length = None

final_time = None

while True:
    if start == 0 and end == 0:
        time.sleep(sleep)
        ohlcv = exchange.fetch_ohlcv(pair, time_frame, since=1499040000000, limit=1000)
        length = len(ohlcv)
        start = 1
        print(length)
        for i in range(length):
            epoch = ohlcv[i][0] / 1000
            human_readable = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(epoch))
            time_stamp = human_readable
            open_price = ohlcv[i][1]
            highest_price = ohlcv[i][2]
            lowest_price = ohlcv[i][3]
            closing_price = ohlcv[i][4]
            volume = ohlcv[i][5]
            c.execute("INSERT INTO '%s' (Time_, Open_, High_, Low_, Close_,Volume_) VALUES (?,?,?,?,?,?)" %(symbol),
                      (time_stamp, open_price, highest_price, lowest_price, closing_price, volume))
            conn.commit()

        if length == 1000:
            new_length = length
            last_time = ohlcv[999][0]
            new_time = last_time
            print(last_time)
        else:
            pass

    elif start == 1 and end == 0:
        time.sleep(sleep)
        ohlcv = exchange.fetch_ohlcv(pair, time_frame, since=new_time, limit=1000)
        length = len(ohlcv)
        print(length)
        for i in range(length):
            epoch = ohlcv[i][0] / 1000
            human_readable = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(epoch))
            time_stamp = human_readable
            open_price = ohlcv[i][1]
            highest_price = ohlcv[i][2]
            lowest_price = ohlcv[i][3]
            closing_price = ohlcv[i][4]
            volume = ohlcv[i][5]
            c.execute("INSERT INTO '%s' (Time_, Open_, High_, Low_, Close_,Volume_) VALUES (?,?,?,?,?,?)" %(symbol),
                      (time_stamp, open_price, highest_price, lowest_price, closing_price, volume))
            conn.commit()
        if length == 1000:
            new_length = length
            last_time = ohlcv[999][0]
            new_time = last_time
            print(last_time)
        else:
            end = 1
            last_time = ohlcv[length-1][0]
            final_time = last_time
            print(final_time)



    elif start == 1 and end == 1:
        print('END')
        break
















