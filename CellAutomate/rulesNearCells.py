from ruleManager import RuleManager

class RulesNearCells(RuleManager):
    """
    Offspring of an abstract RuleManager class, implementing Von Neumann's or Moore's neighbourhood algorithms

    Attributes
    __________
    RuleManager: class
        abstract class

    Methods
    _______
    __init__(rlDict, NeumannFlag)
        >rlDict: dictionary of rules^ used for coloring
        >NeumannFlag: is True for Neumann neighborhood and False for Moore's

    compute(x, y, lifeMap)
        computes the color at cell (x, y)
        with consideration of lifeMap settings
    """

    def __init__(self, rlDict, NeumannFlag):
        self.rules = rlDict
        self.vonNeumanNBH = NeumannFlag

    def compute(self, x, y, lifeMap):
        """
        Computes the designated color at cell (x,y)

        :param x: x coordinate of cell
        :param y: y coordinate of cell
        :param lifeMap:
        :return: colorID of the cell
        """

        colordisp = [0, 0, 0, 0, 0, lifeMap.getCell(x, y)]
        if self.vonNeumanNBH:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i, j) != (0, 0): colordisp[lifeMap.getCell(x + i, y + j)] += 1
        else:
            colordisp[lifeMap.getCell(x, y - 1)] += 1
            colordisp[lifeMap.getCell(x + 1, y)] += 1
            colordisp[lifeMap.getCell(x, y + 1)] += 1
            colordisp[lifeMap.getCell(x - 1, y)] += 1
        if tuple(colordisp) in self.rules:
            return self.rules[tuple(colordisp)]
        else:
            return lifeMap.getCell(x, y)
