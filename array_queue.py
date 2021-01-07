from empty import Empty

class ArrayQueue:
    """A python list based implementation of a Queue ADT"""

    DEFAULT_CAPACITY = 16

    def __init__(self):
        """Creates an empty Queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """returns: the numer of elements in the queue"""
        return self._size

    def is_empty(self):
        """returns: true if the queueis empty, false otherwise"""
        return self._size == 0

    def enqueue(self, e):
        """Adds an element to the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        end = (self._front + self._size) % len(self._data)
        self._data[end] = e
        self._size += 1

    def first(self):
        """returns: the first element in the queue without removing it"""
        if self.is_empty():
            raise Empty('The Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """returns: the element removed from the front of the Queue"""
        if self.is_empty():
            raise Empty('The Queue is empty')
        elem = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return elem

    def _resize(self, c):
        """resizes the queue the a list of size c"""
        old = self._data
        self._data = [None] * c
        front = self._front
        for i in range(self._size):        
            self._data[i] = old[front]
            front = (front + 1) % len(old)
        self._front = 0