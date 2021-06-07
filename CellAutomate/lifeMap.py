from colors import Colors

class LifeMap:
    def __init__(self, size, borderTrough=False):
        self._size = tuple(size)
        self.currentColors = Colors()
        self.connectBorders = borderTrough
        row = [0] * self._size[1]
        self.cellMatrix = [list(row) for i in range(self._size[0])]

    def getSize(self):
        return self._size

    def setCell(self, m, n, colorID):
        self.cellMatrix[m][n] = colorID

    def getCell(self, m, n):
        if self.connectBorders:
            return self.cellMatrix[m % self.getSize()[1]][n % self.getSize()[0]]
        elif 0 <= m < self.getSize()[0] and 0 <= n < self.getSize()[1]:
            return self.cellMatrix[m][n]
        else:
            return 0

    def getCellMatrix(self):
        return self.cellMatrix
