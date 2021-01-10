class _DoublyLinkedBase:
    """A base class represetnting a doubly linked list"""

    #--------------------------------------------------------------
    class _Node:
        """Nonpublic class for string a doyubly linked list node"""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, previous, next):
            self._element = element
            self._prev = previous
            self._next = next
    #--------------------------------------------------------------

    def __init__(self):
        """
        Creates an empty list with head and tail sentinel nodes
        """
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        """returns: the number of elements in the list"""
        return self._size

    def is_empty(self):
        """returns: True if the list is empty, False otherwise"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return the new nod"""
        node = self._Node(e, predecessor, successor)
        predecessor._next = node
        successor._prev = node
        self._size += 1
        return node

    def _delete_node(self, node):
        """Delete a non-sentinel node and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element