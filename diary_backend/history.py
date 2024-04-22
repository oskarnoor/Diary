import os
import datetime

time = datetime.datetime.now()

os.rename("today.txt", f"history/today{time.day}.{time.month}.{time.year}.txt")