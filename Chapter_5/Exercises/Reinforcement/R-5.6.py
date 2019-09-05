import ctypes
"""
Our implementation of insert for the DynamicArray class, as given in Code Fragment 5.5, has the following inefficiency.
In the case when a resize occurs, the resize operation takes time to copy all the elements from an old array to a array,
and then the subsequent loop in the body of insert shifts many of those elements. Give an improved implementation of the
insert method, so that, in the case of a resize, the elements are shifted into their final position during that
operation, thereby avoiding the subsequent shifting.
"""


class DynamicArray:
    # DynamicArray class
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    """Origin function __getitem__"""
    # def __getitem__(self, k):
    #     """Return element at index k."""
    #     if not 0 <= k < self._n:
    #         raise IndexError('invalid index')
    #     return self._A[k]

    """New function __getitem that supports negative indices"""
    def __getitem__(self, k):
        """Return element at index k."""
        """If index < 0, return the content in reversed order"""
        if k >= self._n or k < -1 * self._n:
            raise IndexError('invalid index')
        elif k >= 0:
            return self._A[k]
        else:
            return self._A[self._n + k]

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    # Original version of function _resize
    # def _resize(self, c):
    #     """Resize internal array to capacity c."""
    #     B = self._make_array(c)
    #     for k in range(self._n):
    #         B[k] = self._A[k]
    #     self._A = B
    #     self._capacity = c


    # Refined version of function _resize
    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()


def main():
    array = DynamicArray()
    array.append(1)
    print(array[-1])


if __name__ == '__main__':
    main()
