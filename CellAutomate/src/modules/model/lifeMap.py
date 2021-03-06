"""Interactive map of the cells."""
import sys

sys.path.append("../..")


class LifeMap:
    """
    LifeMap is an interactive class that contains basic information for building colored matrix.

    Attributes
    ----------
    size:
        sets the size of the single tuple in lifeMap

    borderTrough: bool
        Matrix border seettring:
            >TRUE: Enclosed for itself
            >FALSE: Enclosed for emptiness (all out-of-border cells are considered white)

    Methods
    ----------
    getsSize()
        gets the size of the object
    setCell(m,n, colorID)
        sets the colorID in cell (m,n)
    getCell(m,n)
        retrieves the color of the cell with consideration of borders
    getColorMatrix()
        retrieves the "colored" interactive matrix

    """

    def __init__(self, size, borderTrough=False):
        """Initialize class."""
        self._size = tuple(size)
        self.connectBorders = borderTrough
        row = [0] * self._size[1]
        self.cellMatrix = [list(row) for i in range(self._size[0])]

    def getSize(self):
        """Get map size."""
        return self._size

    def setCell(self, m, n, colorID):
        """Set cell color."""
        self.cellMatrix[m][n] = colorID

    def getCell(self, m, n):
        """Get cell color."""
        if self.connectBorders:
            return self.cellMatrix[m % self.getSize()[1]][n % self.getSize()[0]]
        elif 0 <= m < self.getSize()[0] and 0 <= n < self.getSize()[1]:
            return self.cellMatrix[m][n]
        else:
            return 0

    def getCellMatrix(self):
        """Get the cell matrix."""
        return self.cellMatrix

    def setCellMatrix(self, cellMatrix):
        """Set the new cell matrix."""
        self.cellMatrix = cellMatrix
