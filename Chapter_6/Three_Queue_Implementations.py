"""
Three implementations of the ADT Queue introduced in the book.
"""


# raise error
class Empty(Exception):
    pass


class QueueOne:     # the easiest way
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        else:
            return self._data[0]

    def enqueue(self, number):
        self._data.append(number)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        else:
            self._data.pop(0)


class QueueTwo:     # the larger queue
    def __init__(self):
        self._data = []
        self._index = 0
        self._num = 0

    def __len__(self):
        return self._num

    def is_empty(self):
        return self._num == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        else:
            return self._data[self._index]

    def enqueue(self, number):
        self._data.append(number)
        self._num += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        else:
            self._data[self._index] = None
            self._index += 1
            self._num -= 1


class QueueThree:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * QueueThree.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


if __name__ == '__main__':
    q1 = QueueOne()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.dequeue()
    print(q1.first())

    q2 = QueueTwo()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.dequeue()
    print(q2.first())

    q2 = QueueThree()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.dequeue()
    print(q2.first())
