"""Main model of the cell automate."""
from .lifeMap import LifeMap
import itertools as it


class Model:
    """
    This class represents the full model of the system, including the matrix and the set of rules.

    Attributes
    _________
    lMap: class
        lifeMap interactive matrix
    manager: class
        a set of handling algorithms, based on cell's neighbourhood

    Methods
    _______

    setLifeMap()
        sets a new life map for the model
    makeStep()
        makes a one whole step for calculating the next condition of the colored matrix
        according to the designated algorithm set
    getLifeMap()
        gets the used lifeMap

    """

    def __init__(self, lMap, manager):
        """Initialize class."""
        self.lifeMap = lMap
        self.buffer = LifeMap(lMap.getSize())
        self.ruleManager = manager

    def setLifeMap(self, newMap=None):
        """Set life map."""
        if newMap is None:
            self.lifeMap = LifeMap(self.lifeMap.getSize())
        else:
            self.lifeMap = newMap

    def makeStep(self):
        """
        Make a cycle on every cell and calculate its color.

        :return: empty, just makes the changes
        """
        x, y = self.lifeMap.getSize()
        for i, j in it.product(range(x), range(y)):
            self.buffer.setCell(i, j, self.ruleManager.compute(i, j, self.lifeMap))
        self.ruleManager.changeMode()
        self.lifeMap, self.buffer = self.buffer, self.lifeMap

    def getLifeMap(self):
        """Get life map."""
        return self.lifeMap
