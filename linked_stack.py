from empty import Empty

class LinkedStack:
    """A linked list implementation of a Stack ADT"""

    #---------------Nseted Node class----------------
    class _Node:
        """Nonpublic class for storing a linked list Node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #---------------Stack Methods--------------------
    def __init__(self):
        """Creates an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """retruns: the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """returns: true if the stack is empty,  false otherwise"""
        return self._size == 0

    def push(self, e):
        """Adds an element to the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        """returns: the element removed from the top of the stack"""
        if self.is_empty():
            raise Empty('The stack is empty')
        removed = self._head._element
        self._head = self._head._next
        self._size -= 1
        return removed

    def top(self):
        """returns: the element from the top of the stack without removing it"""
        if self.is_empty():
            raise Empty('The stack is empty')
        return self._head._element