from ruleManager import RuleManager

class RulesNearCells(RuleManager):
    """
    -Implementing Von Neumann's or Moore's
    neighbourhood algorithms
    -Set with "NeumannFlag" bool init parameter
    """
    def __init__(self, rlDict, NeumannFlag):
        self.rules = rlDict
        self.vonNeumanNBH = NeumannFlag

    def compute(self, x, y, lifeMap):
        """"""
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
