"""
Exexute the experiment from Code Fragment 5.1
and compare the results on your system to those we report in Code Fragment 5.2
"""

# Code Fragment 5.1
import sys
data = []
for k in range(1000):
    a = len(data)
    b = sys.getsizeof(data)
    if not k:
        a_temp = a
        b_temp = b
    if b > b_temp:
        print('Length: %3d; Size in bytes: %3d' % (a_temp, b_temp))
    a_temp = a
    b_temp = b
    data.append(None)
