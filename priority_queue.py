from empty import Empty
from positional_list import PositionalList

class PriorityQueue:
    """
    Abstract base class for priority queue implementations
    """

    #-------------------------------------------------------------------
    class _Item:
        """
        Composite design pattern - lightweight class stores access count
        _key: the access count
        _value: the value stored by the item
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    #-------------------------------------------------------------------

    def is_empty(self):
        """
        return: True if the Priority Queue is empty, false otherwise
        """
        return len(self) == 0



#------------------Concrete Implementations------------------------------


class UnsortedPriorityQueue(PriorityQueue):
    """
    An implementstion of a PriorityQueue
    Store items in an unsorted list
    Requires searching the entire list when accessing items
    """

    def __init__(self):
        """
        Creates an empty PriorityQueue
        """
        self._data = PositionalList()

    def __len__(self):
        """
        returns: the number of items in the PriorityQueue
        """
        return len(self._data)

    def add(self, key, value):
        """
        Adds a key-value pair to the PriorityQueue
        """
        self._data.add_last(self._Item(key, value))

    def _find_min(self):
        """
        Non-public utility method
        returns: the item with the minimum key
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        minimum = self._data.first()
        walk = self._data.after(minimum)
        while walk is not None:
            if walk.element() < minimum.element():  # __lt__ is implemented by the PriorityQueue class
                minimum = walk
            walk = self._data.after(walk)
        return minimum

    def min(self):
        """
        returns: the (k,v) tuple with the minimum key, without removing it
        """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        removes the minimum (k,v) tuple from the priority queue
        returns: the (k,v) tuple
        """
        p = self._find_min()
        item = self._data.delete(p)     # PositionalList removes and returns item
        return (item._key, item._value)


#--------------------------------------------------------------------------------

class SortedPriorityQueue(PriorityQueue):
    """
    Implementation of a PriorityQueue using a sorted PositionalList
    Adds items to the list in order
    """

    def __init__(self):
        """
        Creates an empty PriorityQueue
        """
        self._data = PositionalList()

    def __len__(self):
        """
        returns: the number of items in the PriorityQueue
        """
        return len(self._data)

    def add(self, key, value):
        """
        Adds a key-value pair to the PriorityQueue
        """
        new_item = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and new_item < walk.element():
            walk = self._data.before(walk)
        if walk is not None:
            self._data.add_after(walk, new_item)
        else:
            self._data.add_first(new_item)

    def min(self):
        """
        returns: the (k,v) tuple with the minimum key, without removing it
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        removes the minimum (k,v) tuple from the priority queue
        returns: the (k,v) tuple
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        p = self._data.first()
        item = self._data.delete(p)
        return (item._key, item._value)

    

    