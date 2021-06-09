"""Colors class."""


class Colors:
    """
    Colors class is a color palette^ expressed in a dictionary.

    The correspondence is two-way (for further convenience)

    Methods
    _______
    __init__(colorSeq)
        >colorSeq: sequence of used collors

    swapColor(self, nameID)
        Swaps the numerical ID for <color>: str

    """

    def __init__(self, colorSeq):
        """Initialize class."""
        colorSeq = list(filter(lambda x: x != '', colorSeq))
        self.colorSeq = colorSeq
        self.colors = {x: i for i, x in enumerate(colorSeq)}
        self.colors.update({i: x for i, x in enumerate(colorSeq)})

    def swapColor(self, nameID):
        """Swap color name for ID."""
        return self.colors[nameID]
