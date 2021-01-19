"""
Supports variations on the Euler Tour Traversal algorithm
"""
from tree import Tree


class EulerTour:
    """
    Abstract base class for performing a Euler Tour of a Tree
    Hook methods _hook_previsit and _hook_postvisit can be overridden by subclasses
    """

    def __init__(self, tree):
        """
        Constructs a EulerTour template for a given tree
        tree: a Tree instance
        """
        self._tree = tree

    def tree(self):
        """
        returns: a reference to the tree being traversed
        """
        return self._tree

    def execute(self):
        """
        Perform the tour and return any result from post visit of the root
        """
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        Performs a tour of the subtree rooted at p
        p: a Position in the Tree
        d: depth of p in the Tree
        path: list of indices of children on path from the root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d + 1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    #----Hook methods to be overridden----

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


#-------------------------Euler Tour subclasses-------------------------

class PreorderPrintIndentedTour(EulerTour):
    """
    Produces an indented preorder list of a Tree's elements
    """
    def _hook_previsit(self, p, d, path):
        print(2 * d * ' ' + str(p.element()))


class PreorderPrintLabeledTour(EulerTour):
    """
    Produces a labeled and indented preorder list of a Tree's elements
    """
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)
        print(2 * d * ' ' + label, str(p.element()))


class ParenthesizeTour(EulerTour):
    """
    Prints aparenthetic representation of a tree
    """
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(', ', end='')
        print(p.element(), end='')
        if not self.tree().is_leaf(p):
            print('(', end='')
    
    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(')', end='')


class BinaryEulerTour(EulerTour):
    """
    Abstract base class for performing Euler Tour of a Binary Tree
    Contains an additional _hook_invisit called after the tour of the left subtree
    """

    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass 


class BinaryLayout(BinaryEulerTour):
    """
    Class for computing the (x,y) cordinates for each node of a binary tree
    """

    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0
        
    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1