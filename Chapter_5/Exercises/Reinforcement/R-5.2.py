"""
Redesign the experiment so that the program outputs only those values of k at which the existing capacity is exhausted.
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
