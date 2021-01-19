from linked_queue import LinkedQueue

class Tree:
    """
    Abstract base class representing a Tree structure
    """

    #---------------------Nested Position class-----------------------------
    class Position:
        """
        An abstraction representing the location of a single element
        """
        def element(self):
            """
            returns: the element stored at the Position
            """
            raise NotImplementedError('must be implemented by a sub-class')

        def __eq__(self, o):
            """
            o: a Position object
            returns: True if o represents the same location, False otherwise
            """
            raise NotImplementedError('must be implemented by a sub-class')

        def __ne__(self, o):
            """
            o: a Position object
            returns: True if o does not represent the same location, False otherwise
            """
            return not (self == other)
    
    #------------------------------Abstract Methods--------------------------------------

    def root(self):
        """
        returns: the Position representing the Tree's root (or None if the Tree is empty)
        """
        raise NotImplementedError('must be implemented by a sub-class')

    def parent(self, p):
        """
        p: a Position in the Tree
        returns: the Position representing p's parent (or None if p is the root)
        """
        raise NotImplementedError('must be implemented by a sub-class')

    def num_children(self, p):
        """
        p: a Position in the Tree
        returns: the number of p's children 
        """
        raise NotImplementedError('must be implemented by a sub-class')

    def children(self, p):
        """
        p: a Position in the Tree
        generates an iteration of p's children
        """
        raise NotImplementedError('must be implemented by a sub-class')    

    def __len__(self):
        """
        returns: the number of elements in the Tree
        """
        raise NotImplementedError('must be implemented by a sub-class')

    #----------------------------Concrete Methods-----------------------------------
    def is_root(self, p):
        """
        p: a Position in the Tree
        returns: True if p is root, False otherwise
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        p: a Position in the Tree
        returns: True if p has no children, False otherwise
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """
        returns: True if the Tree is empty, False otherwise
        """
        return len(self) == 0

    def depth(self, p):
        """
        p: a Position in the Tree
        returns: the depth of p in the Tree
        """
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """
        non-public method
        p: a Position in the Tree
        returns: the height of p in the Tree
        """
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))
    
    def height(self, p=None):
        """
        p: a Position in the Tree
        returns: the height of p in the Tree
        """
        if p is None:
            p == self.root()
        return self._height(p)

    #-----------------------------Tree iteration methods-----------------------------------

    def __iter__(self):
        """
        Generates an iteration of the Tree's elements
        """
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """
        Generates a preorder traversal of the Positions in the Tree
        """
        if not self.is_empty():
            for p in self._sub_preorder(self.root()):
                yield p

    def _sub_preorder(self, p):
        """
        Generates a preorder traversal of the Positions in the subtree rooted at p
        p: a Position in the Tree
        """
        yield p
        for c in self.children(p):
            for other in self._sub_preorder(c):
                yield other

    def positions(self):
        """
        Generates an iteration of the Tree's Positions using preorder
        """
        return self.preorder()

    def postorder(self):
        """
        Genreates a postorder traversal of the Tree's Positions
        """
        if not self.is_empty():
            for p in self._sub_postorder(self.root()):
                yield p

    def _sub_postorder(self, p):
        """
        Generates a postorder traversal of the subtree rooted at p
        """
        for c in self.children(p):
            for other in self._sub_postorder(c):
                yield other
        yield p

    def breadth_first(self):
        """
        Generates a breadth first traversal of a Tree's positions
        """
        if not self.is_empty():
            q = LinkedQueue()
            q.enqueue(self.root())
            while not q.is_empty():
                for c in self.children(q.first()):
                    q.enqueue(c)
                yield q.dequeue()

