from empty import Empty

class LinkedQueue:

    #---------------Nseted Node class----------------
    class _Node:
        """Nonpublic class for storing a linked list Node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        """returns: the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """returns: true if the queue is empty, false otherwise"""
        return self._size == 0

    def enqueue(self, e):
        """Adds an element to the queue"""
        node = self._Node(e, None)
        if self.is_empty():
            self._front = node
        else:
            self._rear._next = node
        self._rear = node
        self._size += 1


    def dequeue(self):
        """returns: the element removed from the front of the queue"""
        if self.is_empty():
            raise Empty('The queue is empty')
        removed = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.is_empty():
            self._rear = None
        return removed


    def first(self):
        """returns: the element at the front of the queue without removing it"""
        if self.is_empty():
            raise Empty('The queue is empty')
        return self._front._element

    