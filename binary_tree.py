class  BinaryTree(Tree):
    """
    Abstract base class representing a binary tree structure
    """

    #--------------------Abstract methods-------------------
    def left(self, p):
        """
        p: a Position in the Tree
        returns: the left child of Position p
        """
        raise NotImplementedError('must be implemented by a sub-class')

    
    def right(self, p):
        """
        p: a Position in the Tree
        returns: the right child of Position p
        """
        raise NotImplementedError('must be implemented by a sub-class')

    #---------------------Concrete Methods---------------------
    def sibling(self, p):
        """
        p: a Position in the Tree
        returns: a Position representing p's sibling (or None if p has no sibling)
        """
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        """
        p: a Position in the Tree
        generates an iteration of Positions representing p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)