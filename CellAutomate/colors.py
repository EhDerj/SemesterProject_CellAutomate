class Colors:
    """
    -Basic color ID palette dictionary
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
        """
        Color ID swapping
        ColorID -> Color Name
        """
        return self.colors[nameID]