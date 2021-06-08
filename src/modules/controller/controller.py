
class Controller:
  '''Controller class.'''
  
  def __init__(self, model):
    '''Initiates controller with model relation.'''
    self.model = model

  def getLifemapSize(self):
    '''Gets life map size.'''
    currentLifemap = self.model.getLifeMap()
    return currentLifemap.getSize()

