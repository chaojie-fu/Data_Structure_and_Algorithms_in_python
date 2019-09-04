"""
Exexute the experiment from Code Fragment 5.1
and compare the results on your system to those we report in Code Fragment 5.2
"""

# Code Fragment 5.1
import sys
data = []
for k in range( 10 ):
    a = len(data)
    b = sys.getsizeof(data)
#   print('Length: ', a, 'Size in bytes: ', b)
    print('Length: %3d; Size in bytes: %3d' % (a, b))
    data.append(None)
