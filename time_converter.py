import calendar
import time

## Epoch Converter to Human Readable
epoch = 1499040000000 / 1000
#human_readable = time.strftime("%Y-%m-%d %H:%M:%S +0000",time.gmtime(epoch))
human_readable = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(epoch))
print(human_readable)


## Human Readable to Epoch
epoch = calendar.timegm(time.strptime('2017-07-03 00:00:00', '%Y-%m-%d %H:%M:%S'))
converted_to_ms = (epoch * 1000)
print(converted_to_ms)
#%%