from doubly_linked_list import _DoublyLinkedBase
from empty import Empty

class Dequeue(_DoublyLinkedBase):
    """
    Double-ended queue implemented with a doubly linked list
    """

    def first(self):
        """
        returns: the first element in the dequeue without removing it
        raises: an Empty exception if the dequeue is empty
        """
        if self._size == 0:
            raise Empty('Dequeue is empty')
        return self._head._next._element

    def last(self):
        """
        returns: the last element in the dequeue without removing it
        raises: an Empty exception if the dequeue is empty
        """
        if self._size == 0:
            raise Empty('Dequeue is empty')
        return self._tail._prev._element
    
    def insert_first(self, e):
        """
        Inserts an element at the front of the dequeue
        """
        self._insert_between(e, self._head, self._head._next)

    def insert_last(self, e):
        """
        Inserts an element at the end of the queue
        """
        self._insert_between(e, self._tail._prev, self._tail)

    def delete_first(self):
        """
        Removes and returns the first element in the dequeue
        raises: an Empty exception if the dequeue is empty
        """
        if self._size == 0:
            raise Empty('Dequeue is empty')
        return self._delete_node(self._head._next)

    def delete_last(self):
        """
        Removes and returns the last element in the dequeue
        raises: an Empty exception if the dequeue is empty
        """
        if self._size == 0:
            raise Empty('Dequeue is empty')
        return self._delete_node(self._tail._prev)