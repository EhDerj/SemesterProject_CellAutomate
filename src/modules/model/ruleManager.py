from abc import ABC, abstractmethod

class RuleManager(ABC):

    @abstractmethod
    def compute(self, x, y, lifeMap):
        """Abstract method"""
