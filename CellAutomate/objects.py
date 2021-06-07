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
    def compute(self, x, y, lifeMap):
        """Abstract method"""


class RulesNearCells(RuleManager):
    def __init__(self, rlDict, NeumannFlag):
        self.rules = rlDict
        self.vonNeumanNBH = NeumannFlag

    def compute(self, x, y, lifeMap):
        colordisp = [0, 0, 0, 0, 0, lifeMap.getCell(x, y)]
        if self.vonNeumanNBH:
            for i in range(-1, 1):
                for j in range(-1, 1):
                    if (i, j) != (x, y): colordisp[lifeMap.getCell(x + i, y + j)] += 1
        else:
            colordisp[lifeMap.getCell(x, y - 1)] += 1
            colordisp[lifeMap.getCell(x + 1, y)] += 1
            colordisp[lifeMap.getCell(x, y + 1)] += 1
            colordisp[lifeMap.getCell(x - 1, y)] += 1
        if tuple(colordisp) in self.rules:
            return self.rules[tuple(colordisp)]
        else:
            return lifeMap.getCell(x, y)


class RulesSquares(RuleManager):
    def __init__(self, rlDict):
        self.rules = rlDict
        self.computed = dict()

    def compute(self, x, y, lifeMap):
        if (x, y) in self.computed:
            n = self.computed[(x, y)]
            del self.computed[(x, y)]
            return n
        tup = (
            lifeMap.getCell(x+0, y+0),
            lifeMap.getCell(x+1, y+0),
            lifeMap.getCell(x+0, y+1),
            lifeMap.getCell(x+1, y+1),
        )
        if tup in self.rules:
            a, b, c, d = self.rules[tup]
        else:
            a, b, c, d = tup
        self.computed[(x+1, y+0)] = b
        self.computed[(x+0, y+1)] = c
        self.computed[(x+1, y+1)] = d
        return a