

class Controller:
  
  def __init__(self, model):
    self.model = model

  def getLifemapSize(self):
    currentLifemap = self.model.getLifeMap()
    return currentLifemap.getSize()

