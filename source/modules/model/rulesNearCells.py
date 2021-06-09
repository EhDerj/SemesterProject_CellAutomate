from .ruleManager import RuleManager


class RulesNearCells(RuleManager):
    """
    Offspring of an abstract RuleManager class, implementing Von Neumann's
    or Moore's neighbourhood algorithms

    Attributes
    __________
    RuleManager: class
        abstract class

    Methods
    _______
    __init__(colorsNum, defaultColor, flagMoore, rules)
        >colorsNum: number of colors in used rules
        >defaultColor: colorID which return default or None for no default action
        >flagMoore: is True for Moore neighborhood and False for vonNeumann's
        >rules: dictionary of rules^ used for coloring

    compute(x, y, lifeMap)
        computes the color at cell (x, y)
        with consideration of lifeMap settings

    changeMode()
        does nothing in this manager type
    """

    def __init__(self, colorsNum, defaultColor, flagMoore, rules):
        self.colorsNum = colorsNum
        self.defaultColor = defaultColor
        self.flagMoore = flagMoore
        self.rules = rules

    def compute(self, x, y, lifeMap):
        """
        Computes the designated color at cell (x,y)

        :param x: x coordinate of cell
        :param y: y coordinate of cell
        :param lifeMap:
        :return: colorID of the cell
        """

        colordisp = [0] * self.colorsNum
        if self.flagMoore:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i, j) != (0, 0):
                        colordisp[lifeMap.getCell(x + i, y + j)] += 1
        else:
            colordisp[lifeMap.getCell(x, y - 1)] += 1
            colordisp[lifeMap.getCell(x + 1, y)] += 1
            colordisp[lifeMap.getCell(x, y + 1)] += 1
            colordisp[lifeMap.getCell(x - 1, y)] += 1

        colordisp = (lifeMap.getCell(x, y), tuple(colordisp))
        if colordisp in self.rules:
            return self.rules[colordisp]
        elif self.defaultColor is None:
            return lifeMap.getCell(x, y)
        else:
            return self.defaultColor

    def changeMode(self):
        """
    This type of neighbouhood have only one mode
        """
        pass
