from doubly_linked_list import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """
    A sequential container of elements allowing positional access
    """

    #-------------------Nested Position class-----------------------
    class Position:
        """
        An abstraction representing the location of a single element
        """

        def __init__(self, container, node):
            """
            Constructor - should not be onvoked by user
            """
            self._container = container
            self._node = node

        def element(self):
            """
            returns: the element stored at this position
            """
            return self._node._element

        def __eq__(self, other):
            """
            returns: True if other is a Position representing the same location
            """
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            """
            returns: True if other does not represent the same location
            """
            return not(self == other)

    #-----------------------Utility methods-------------------------------
    def _validate(self, p):
        """
        return: position p's node, or raises an error if p is invalid
        """
        if not isinstance(p, self.Position):
            raise TypeError('p is not a Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:  # _next set to None is default for defunct nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """
        returns: a Position instance for the given node
        """
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self, node)

    #------------------------------Accessors------------------------------------
    def first(self):
        """
        returns: the first Position in the list or None if empty
        """
        return self._make_position(self._head._next)

    def last(self):
        """
        returns: the last Position in the list or None if empty
        """
        return self._make_position(self._tail._prev)

    def before(self, p):
        """
        returns: the Position before Position p or None if p i first
        """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        returns: the Position after Position p or None if p is last
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """
        Generates a forward iteration of the elements in the list
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #-------------------------Mutators----------------------------
    def _insert_between(self, e, predecessor, successor):
        """
        Adds an element between two existing nodes
        returns: a new Position
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """
        Adds an element to the front of the list
        returns: a new Position
        """
        node = super()._insert_between(e, self._head, self._head._next)
        return self._make_position(node)

    def add_last(self, e):
        """
        Adds an element to the end of the list
        returns: a new Position
        """
        node = super()._insert_between(e, self._tail._prev, self._tail)
        return self._make_position(node)

    def add_before(self, p, e):
        """
        Adds an element after a given Position
        returns: a new Postion
        """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        """
        Adds an element after a given Position
        returns: a new Postion
        """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """
        Removes the Position p
        returns: p's element
        """
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        """
        Replaces the element at Position p with e
        returns: the element formerly at p
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def sort(self):
        """
        Sorts the items in the PositionalList into non-decreasing order
        Using insertion sort
        """
        if self._size > 1:
            index = self.first()
            while index != self.last():
                j = self.after(index)
                value = j.element()
                if value > index.element():
                    index = j
                else:
                    i = index
                    while i != self.first() and self.before(i).element() > value:
                        i = self.before(i)
                    self.delete(j)
                    self.add_before(i, value)
