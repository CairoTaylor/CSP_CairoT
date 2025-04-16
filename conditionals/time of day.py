# Cairo Taylor, Time of Day

import time
current = time.time()
now = time.ctime(current)
local_time = time.localtime(current)
minutes = local_time.tm_min
hours = local_time.tm_hour

if hours == 12:
    print("It's noontime!")
elif hours >= 2 and hours < 6:
    print("Dawn is upon you! You sure do get up early!")
elif hours >= 6 and hours < 12:
    print("Good Morning!")
elif hours >= 12 and hours < 20:
    print("Good evening!")
elif hours >= 20 and hours < 22:
    print("It's getting late!")
else:
    print("Go to sleep, it's nighttime.")