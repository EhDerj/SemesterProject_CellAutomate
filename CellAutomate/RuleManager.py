from abc import ABC, abstractmethod


class RuleManager(ABC):
    def __init__(self):
        self.Rules = []

    @abstractmethod
    def Compute(self):
        pass
