class ColorMap:
    """
    -lifeMap resulting matrix
    -Transfered to view.py
    -Remains constant on single iteration
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

