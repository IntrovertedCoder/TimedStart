# TimedStart
A simpler way to schedule a python script.

Usage:

import TimedStart

import time

time.sleep(min(TimedStart.timelefthourmin(['8:30', '9:30']))  # Will sleep for the ammount of seconds until the system time is 8:30 or 9:30.

Returns the ammount of time before the system clock reaches given times.

Also includes:

timeleftmin([30, 60])

timeleftminsec(['5:30', '7:30'])

timelefthour([14, 17])  Returns the ammount of time before the hour hits the selected numbers.

timelefthourmin(['6:30, 7:30])

timelefthourminsec(['3 30 45', '4:30:45'])
