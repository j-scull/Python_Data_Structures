from empty import Empty

class ArrayStack:
    """A python list based implementation of a Stack ADT"""

    def __init__(self):
        """creates an empty stack"""
        self._data = []

    def __len__(self):
        """returns: the number of elements in the stack"""
        return len(self._data)

    def isEmpty(self):
        """returns: true if the stack is empty, false otherwise"""
        return len(self._data) == 0

    def push(self, e):
        """adds an element to the top of stack"""
        self._data.append(e)

    def pop(self):
        """
        returns: the element remove from the top of the stack
        raises: an Empty exception if the stack is empty
        """
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def top(self):
        """
        returns: the element at the top of the stack without removing it
        raises: an Empty exception if the stack is empty
        """
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._data[-1]


