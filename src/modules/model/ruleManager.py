from abc import ABC, abstractmethod

class RuleManager(ABC):
    """
    Abstract class for creating two offspring rule classes

    Attributes
    __________
    ABC:
        standart abstract class attribute

    Methods
    _______
    compute(x, y, lifeMap)
        abstract method used in RNC.py and RS.py for computing the color at cell (x, y)
        with consideration of lifeMap settings

    changeMode()
        abstract method used in RNC.py and RS.py for changing mode of rule manager
        for each automate step
    """

    @abstractmethod
    def compute(self, x, y, lifeMap):
        """Abstract method for usage in class offsprings"""

    @abstractmethod
    def changeMode(self):
        """Abstract method for usage in class offsprings"""
