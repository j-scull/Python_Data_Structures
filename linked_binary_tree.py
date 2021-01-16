from binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """
    Linked representation of a binary tree structure
    """
    
    #-----------------------------Nested Node Class--------------------------------
    class _Node:
        """
        Non-public class for storing a node
        """
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    #--------------------------Nested Position Class-------------------------------
    class Position(BinaryTree.Position):
        """
        An abstraction representing the location of a single element
        """

        def __init__(self, container, node):
            """
            Constructor - should not be invoked by user
            """
            self._container = container
            self._node = node

        def element(self):
            """
            returns: the element stored at this Position
            """
            return self._node._element

        def __eq__(self, other):
            """
            returns: True if other represents the same Position, otherwise False
            """
            return type(other) is type(self) and self._node is other._node

    #----------------------------Utility Methods-----------------------------------
    def _validate(self, p):
        """
        returns: the node associated with Position p if p is valid
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be a Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node: # convention for defunct node
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """
        returns: a Position instance of a node
        """
        return self.Position(self, node) if node is not None else None

    #------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructs an empty Binary Tree
        """
        self._root = None
        self._size = 0

    #--------------------------Public Accessors------------------------------------

    def __len__(self):
        """
        returns: the number of elements in the Binary Tree
        """
        return self._size

    def root(self):
        """
        returns: the root Position of the Tree
        """
        return self._make_position(self._root)

    def parent(self, p):
        """
        p: a Position
        returns: p's parent (or None if p is root)
        """
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """
        p: a Position
        returns: p's left child (or None if p has no left child)
        """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """
        p: a Position
        returns: p's right child (or None if p has no right child)
        """
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """
        p: a Position
        returns: the number of p's children
        """
        node = self._validate(p)
        num = 0
        if node._left is not None:
            num += 1
        if node._right is not None:
            num += 1
        return num

    def _add_root(self, e):
        """
        Places e at the root of an empty tree
        e: an element
        returns: the new Position
        raises: a ValueError if the tree is non-empty
        """
        if self._root is not None:
            raise ValueError('Root already exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """
        Creates a new left child for p, storing e
        p: a Position in the binary tree
        e: an element
        returns: the Position of the new node
        raises: a ValueError if p is invalid or p already has a left child
        """
        node = self._validate(p)
        if node._left is not None:
            raise('Left child already exists')
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """
        Creates a new right child for p, storing e
        p: a Position in the binary tree
        e: an element
        returns: the Position of the new node
        raises: a ValueError if p is invalid or p already has a right child
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child already exists')
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        """
        Replaces the element stored at p with e
        p: a Position in the binary tree
        e: an element
        returns: the element previously stored at p
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        Deletes p and replaces it with its child if any
        p: a Position in the binary tree
        returns: the element that was stored at p
        raises: a ValueError if p is invalid or has two children 
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Cannot delete, position has two children')
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convention for defunct node
        return node._element

    def _attach(self, p, t1, t2):
        """
        Attaches t1 and t2 as the left and right subtrees rooted at p
        p: an external Position in the Binary Tree
        t1, t2: two subtrees
        raises: a ValueError if p is not a leaf node
                a TypeError if t1 and t2 are not the same type of Tree
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
    