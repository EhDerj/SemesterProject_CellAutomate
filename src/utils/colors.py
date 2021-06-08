class Colors:
    """
    Colors class is a color palette^ expressed in a dictionary
    The correspondence is two-way (for further convenience)

    Methods
    _______
    __init__(colorSeq)
        >colorSeq: sequence of used collors

    swapColor(self, nameID)
        Swaps the numerical ID for <color>: str
    """
    def __init__(self, colorSeq):
        self.colors = { colorSeq[i] : i for i in range(len(colorSeq)) }
        self.colors.update({ colorSeq[i] : i for i in self.colors })

    def swapColor(self, nameID):
        return self.colors[nameID]