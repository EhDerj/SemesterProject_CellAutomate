from abc import ABC, abstractmethod

class RuleManager(ABC):
    """
    Abstract class for creating two offspring rule classes
    """
    @abstractmethod
    def compute(self, x, y, lifeMap):
        """Abstract method"""
