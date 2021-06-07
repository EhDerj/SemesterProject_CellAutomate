from ruleManager import RuleManager

class RulesSquares(RuleManager):
    def __init__(self, rlDict):
        self.rules = rlDict
        self.computed = dict()

    def compute(self, x, y, lifeMap):
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
        else:
            a, b, c, d = tup
        self.computed[(x+1, y+0)] = b
        self.computed[(x+0, y+1)] = c
        self.computed[(x+1, y+1)] = d
        return a