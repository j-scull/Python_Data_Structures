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

    
#----------------------------------------------------------------------------------

class HeapPriorityQueue(PriorityQueue):
    """
    An implementation of a Priorrity Queue using an array based heap data structure
    -------------------------------------------------------------------------------
    uses the _Item class from PriorityQueue
    """


    #--------Non-Public methods-------

    #       0
    #     /   \  
    #    1     2
    #   / \   /  \
    #  3   4 5    6

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        """
        Swaps the the elements stored at indexex i and j 
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        """
        Performed after inserting a new element into the heap
        Restores heap-order property
        """
        parent = self._parent(i)
        if i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def _downheap(self, i):
        """
        Performed after removing the minimum element from the heap
        Restores heap-order property
        """
        if self._has_left(i):
            left = self._left(i)
            smallest = left
            if self._has_right(i):
                right = self._right(i)
                if self._data[right] < self._data[left]:
                    smallest = right
            if self._data[smallest] < self._data[i]:
                self._swap(i, smallest)
                self._downheap(smallest)

    def _heapify(self):
        """
        Performs bottom-up construction for a new heap
        """
        #       0             0             X
        #     /   \         /   \         /   \  
        #    0     0       X     X       X     X
        #   / \   /  \    / \   /  \    / \   /  \
        #  X   X X    X  X   X X    X  X   X X    X
        start = self._parent(len(self) - 1)   # starts at the parent of the last leaf
        for i in range(start, -1, -1):
            self._downheap(i)

    #--------Public methods-----------

    def __init__(self, contents=()):
        """
        Create an new Priority Queue
        If contents is given creates a heap using bottom up construction, 
        otherwise creates an empty heap

        contents: an iterable sequence of (k,v) tuples
        """
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        """
        returns: the number of elements in the priority queue
        """
        return len(self._data)

    def add(self, key, value):
        """
        Adds a key-value pair to te priority queue
        """
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)


    def min(self):
        """
        returns: the key-value pair with the minimum key without removal
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """
        returns: the key-value pair with the minimal key removed from the priority queue
        """
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)


    
