class ColorMap:
    """
    ColorMap class is a class that transfers fixed resulting matrix
    retrieved from liveMap to view.py module

    Attributes
    ----------
    lifeMap: class
        an interactive matrix^ representing the current state of the system

    Methods
    -------
    getSize()
        retrieves the size of the class object
    getColor(m,n)
        retrieves the color of cell with coordinates (m,n)
    getColorMatrix()
        retrieves the "colored" matrix
    """
    def __init__(self, lifeMap):
        self._size = lifeMap.getSize()
        self.colorMatrix = []
        for i in range(self._size[1]):
            self.colorMatrix.append([])
            for j in range(self._size[0]):
                self.colorMatrix[i].append(lifeMap.currentColors.swapColor(lifeMap.getCell(i, j)))

    def getSize(self):
        return self._size

    def getColor(self, m, n):
        return self.colorMatrix[m][n]

    def getColorMatrix(self):
        return self.colorMatrix

