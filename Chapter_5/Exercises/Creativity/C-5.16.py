"""
Implement a pop method for the DynamicArray class, given in Code Fragment 5.3, that removes the last element of the
array, and that shrinks the capacity, N, of the array by half any time the number of elements in the array goes below
N/4
"""
import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        if self._n == 0:
            raise IndexError('invalid index')
        self._n -= 1
        if self._n <= self._capacity // 4:
            self._capacity //= 2


    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    array = DynamicArray()
    for j in range(10):
        array.append(j)
    print(array._capacity)
    print(array._n)
    while array._n > 0:
        array.pop()
        print(array._capacity)
        print(array._n)
        print('-------------------------------')