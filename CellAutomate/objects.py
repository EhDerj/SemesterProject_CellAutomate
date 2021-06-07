from abc import ABC, abstractmethod


class Colors:

    def __init__(self):
        self.colors = {
            'White': 0,
            'Black': 1,
            'Red': 2,
            'Yellow': 3,
            'Blue': 4,
            0: 'White',
            1: 'Black',
            2: 'Red',
            3: 'Yellow',
            4: 'Blue'
        }

    def swapColor(self, nameID):
        return self.colors[nameID]


class LifeMap:
    def __init__(self, size, borderTrough=False):
        self._size = tuple(size)
        self.currentColors = Colors()
        self.connectBorders = borderTrough
        self.cellMatrix = [[0] * self._size[0]] * self._size[1]

    def getSize(self):
        return self._size

    def setCell(self, m, n, colorID):
        self.cellMatrix[m][n] = colorID

    def getCell(self, m, n):
        if self.connectBorders:
            return self.cellMatrix[m % self.getSize()[1]][n % self.getSize()[0]]
        elif 0 <= m < self.getSize()[1] and 0 <= n < self.getSize()[0]:
            return self.cellMatrix[m][n]
        else:
            return 0

    def getCellMatrix(self):
        return self.cellMatrix


class ColorMap:
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


class RuleManager(ABC):

    @abstractmethod
    def compute(self):
        """Abstract method"""
        """Computes current cell color according to rules"""
