# import datetime
# from math import floor

# import time 
# currenttime = datetime.datetime.now()
# hours = currenttime.strftime('%H')
# minutes = currenttime.strftime('%M')

# today = currenttime.day
# month = currenttime.month

# # print(hours)
# # print(minutes)
# # print(today)
# # print(month)


# position = 2.95450
# # floor_position = floor(position)
# int_position = int(position)
# # print(int_position)
# ct = datetime.datetime.now()
# # time.sleep(60)
# year = 2022
# month = 8
# today = 21
# hours = 12

# sell_time = datetime.datetime(year, month, today, hours, 5, 00)
# sell_time_2 = datetime.datetime(year, month, today, hours, 5, 30)
# print(type(currenttime))
# # print(ct)
# # print(ct-currenttime)
# curr = sell_time_2 - sell_time
# # print(sell_time_2 - sell_time)
# # print(type(curr))


# letter = "asd"
# letter2 = "tasdsdasdos"
# a = 11.233433
# b = 3333.313344426235
# xx = "TRUE"
# yy = "FALSE"
# print("{: >12} 93.0293 {: >12.2f} yolo {: >12}".format(letter, a, xx))
# print("{: >12} 93.0293 {: >12.2f} yolo {: >12}".format(letter2, b, yy))



# d = datetime.time(0,5,0)
# print(datetime.datetime.now())

# import pandas as pd

# alpha = [1,2,3,4,5,6,7,8,9]

# df_alpha = pd.DataFrame(alpha)
# X = df_alpha.rolling(3).mean()
# # print(X)

# shifted = df_alpha.shift(-2)
# print(shifted)

# import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


import pandas as pd
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})
print(df)
print(df2)
# df = df.append(df2, reset_index=True)
df = pd.concat([df, df2], ignore_index=True)
print(df)