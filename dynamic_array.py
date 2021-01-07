import ctypes

class DynamicArray:
    """
    A dynamic array class - a simplified version of a python list
    """

    def __init__(self):
        """
        Creates an empty array
        """
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)


    def __len__(self):
        """
        returns: the number of items in the array
        """
        return self._n


    def append(self, obj):
        """
        Adds an object to the array
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1


    def __getitem__(self, i):
        """
        returns: the object at index i
        """
        if not 0 <= i < self._n:
            raise IndexError('Invalid index')
        return self._A[i]


    def insert(self, i, obj):
        """
        inserts an object at index i
        """
        if not 0 <= i < self._n:
            raise IndexError('Invalid index')
        if self._n == self._capacity:
            self._resize(2 * self.capacity)
        for j in range(self._n, i, -1):
            self._A[j] = self._A[j-1]
        self._A[i] = obj
        self._n += 1


    def remove(self, obj):
        """
        removes the first occurence of an object from an array
        """
        for j in range(0, self._n):
            if self._A[j] == obj:
                for i in range(j, self._n - 1):
                    self._A[i] = self._A[i+1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('Value not found')


    def _resize(self, c):
        """
        resize the array to capacity c
        """
        B = self._make_array(c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c


    def _make_array(self, c):
        """ 
        returns: a new aray with capacity c
        """
        return (c * ctypes.py_object)()