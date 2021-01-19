class Coordinate:
    """
    Represents a (x,y) coordinate
    """

    def __init__(self, x, y):
        """
        Constructs a Coordinate
        x: the position on the x-axis
        y: the position on the y-axis
        """
        self._x = x
        self._y = y

    def getX(self):
        """
        returns: the x coordinate
        """
        return self._x

    def getY(self):
        """
        returns: the y coordinate
        """
        return self._y

    def setX(self, x):
        """
        sets the x coordinate
        """
        self._x = x

    def setY(self, y):
        """
        sets the y coordinate
        """
        self._y = y

    def distance(self, other):
        """
        returns: the distance to another coordinate
        """
        if isinstance(other, tuple) :
            return ((self._x - other[0])**2 + (self._y - other[1])**2)**0.5
        elif isinstance(other, Coordinate):
            return ((self._x - other.getX())**2 + (self._y - other.getY())**2)**0.5
        else:
            raise ValueError('Not a valid Coordinate')

    def __str__(self):
        """
        returns: a String representation of the coordinate
        """
        return '(' + str(self._x) + ',' + str(self._y) + ')'

    