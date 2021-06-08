class Colors:
    """
    Colors class is a basic 5 color palette^ expressed in a dictionary
    The correspondence is two-way (for further convenience)

    Methods
    _______
    swapColor(self, nameID)
        Swaps the numerical ID for <color>: str
    """
    def __init__(self):
        self.colors = {
            'White': 0,
            'Black': 1,
            'Red': 2,
            'Yellow': 3,
            'Blue': 4,
            0: 'White',
            1: 'Black',
            2: 'Red',
            3: 'Yellow',
            4: 'Blue'
        }

    def swapColor(self, nameID):
        return self.colors[nameID]