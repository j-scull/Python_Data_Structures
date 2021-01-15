from empty import Empty

class CircularQueue:
    """
    Queue implementation using a circularly linked list
    """

    #------------------Nested Node class--------------------
    class _Node:
        """Nonpublic class for storing a linked list Node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    #-------------------------------------------------------

    def __init__(self):
        """
        Creates an empty Queue
        """
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """
        returns: the number of elements in the Queue
        """
        return self._size

    def is_empty(self):
        """
        returns: True if the Queue is empty, False otherwise
        """
        return self._size == 0

    def first(self):
        """
        returns: the first element in the Queue without removing it
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """
        returns: the element removed from the front of the queue
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        if self._size == 1:
            self._tail._next = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return head._element

    def enqueue(self, e):
        """
        Adds an element to the end of the queue
        """
        node = self._Node(e, None)
        if self._size == 0:
            node._next = node
        else:
            node._next = self._tail._next
            self._tail._next = node
        self._tail = node
        self._size += 1

    def rotate(self):
        """
        Rotates the front element to the back of the queue
        """
        if self._size > 0:
            self._tail = self._tail._next