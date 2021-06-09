"""Margulis rules handler class."""
from .ruleManager import RuleManager


class RulesSquares(RuleManager):
    """
    Offspring of an abstract RuleManager class, implementing Margulis-block neighbourhood algorithms.

    Attributes
    __________
    RuleManager: class
        abstract class

    Methods
    _______
    __init__(defaultColor, rules)
        >defaultColor: colorID which return default or None for no default action
        >rules: dictionary of rules^ used for coloring

    compute(x, y, lifeMap)
        computes the color at cell (x, y)
        with consideration of lifeMap settings

    changeMode()
        move computing grid for 1 cell diagonal

    """

    def __init__(self, defaultColor, rules):
        """Initialize class."""
        self.defaultColor = defaultColor
        self.rules = rules
        self.computed = dict()
        self.shift = True

    def compute(self, x, y, lifeMap):
        """
        Compute current cell's designated color using Margulis-block algorithm.

        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        :param lifeMap: lifeMap class representing the colored matrix
        :return: designated colorID of the cell
        """
        if (x, y) in self.computed:
            n = self.computed[(x, y)]
            del self.computed[(x, y)]
            return n
        grid = (
            (x + 0, y + 0),
            (x + 1, y + 0),
            (x + 0, y + 1),
            (x + 1, y + 1),
        ) if self.shift else (
            (x - 1, y - 1),
            (x + 0, y - 1),
            (x - 1, y + 0),
            (x + 0, y + 0),
        )
        tup = (
            lifeMap.getCell(*grid[0]),
            lifeMap.getCell(*grid[1]),
            lifeMap.getCell(*grid[2]),
            lifeMap.getCell(*grid[3]),
        )
        if tup in self.rules:
            tup = self.rules[tup]
        elif self.defaultColor is not None:
            tup = (self.defaultColor,) * 4
        (self.computed[grid[0]],
         self.computed[grid[1]],
         self.computed[grid[2]],
         self.computed[grid[3]]) = tup
        n = self.computed[(x, y)]
        del self.computed[(x, y)]
        return n

    def changeMode(self):
        """Change if it's needed to shift computing grid."""
        self.shift = not self.shift
        self.computed = dict()
