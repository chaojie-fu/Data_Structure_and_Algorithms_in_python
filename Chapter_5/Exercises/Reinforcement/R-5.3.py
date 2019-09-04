"""
Modify the experiment from Code Fragment 5.1 in order to demonstrate that Python's list class
occasionally shrinks the size of its underlying array when elements are poped from a list.
"""

import sys
data = [j for j in range(100)]
for k in range(99, -1, -1):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: %3d; Size in bytes: %3d' % (a, b))
    data.pop()

