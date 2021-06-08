from .ruleManager import RuleManager

class RulesSquares(RuleManager):
    """
    Offspring of an abstract RuleManager class, implementing Margulis-block neighbourhood algorithms

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
    """
    def __init__(self, defaultColor, rules):
        self.defaultColor = defaultColor
        self.rules = rules
        self.computed = dict()

    def compute(self, x, y, lifeMap):
        """
        This method computes current cell's designated color using Margulis-block algorithm

        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        :param lifeMap: lifeMap class representing the colored matrix
        :return: designated colorID of the cell
        """
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
        elif self.defaultColor is None:
            a, b, c, d = tup
        else:
            a = b = c = d = self.defaultColor
        self.computed[(x+1, y+0)] = b
        self.computed[(x+0, y+1)] = c
        self.computed[(x+1, y+1)] = d
        return a
        