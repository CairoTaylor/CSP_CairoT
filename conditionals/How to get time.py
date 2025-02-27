# Cairo Taylor, How to get time

import time
# First instance of time: print(time.gmtime(0))
# Current time in seconds since gmtime: print(time.time())
current = time.time()

# Current time as we are used to seeing it
now = time.ctime(current)
print(now)

# Get just the hour
local_time = time.localtime(current)
minutes = local_time.tm_min
print(minutes)
hours = local_time.tm_hour
print(hours)

