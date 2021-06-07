from objects import LifeMap
import itertools as it

class Model:
    def __init__(self, lMap, manager):
        self.lifeMap = lMap
        self.buffer = LifeMap(lMap.getSize())
        self.ruleManager = manager

    def setLifeMap(self, newMap):
        self.lifeMap = newMap

    def makeStep(self):
        x, y = self.lifeMap.getSize()
        for i, j in it.product(range(x), range(y)):
            self.buffer.setCell(i, j, self.ruleManager.compute(i, j, self.lifeMap))
        self.lifeMap, self.buffer = self.buffer, self.lifeMap

    def getLifeMap(self):
        return self.lifeMap