import modules.model.model
import modules.model.ruleManager
import modules.model.lifeMap
from os import listdir
from os.path import isfile, join

class Controller:
  '''Controller class.'''
  
  def __init__(self, model):
    '''Initiates controller with model relation.'''
    self.model = model

  def getLifemapSize(self):
    '''Gets life map size.'''
    currentLifemap = self.model.getLifeMap()
    return currentLifemap.getSize()

  def getMap(self):
    '''Returns LifeMap'''
    currentLifemap = self.model.getLifeMap()
    return currentLifemap

  def getRuleFiles(self):
    onlyfiles = [f for f in listdir('../../rules') if isfile(join('../../rules', f))]
    retVal = []
    for i in onlyfiles:
      k = 0
      with open(i, "r") as f:
        col = f.readline().replace("\n", " ").split(" ")
        self.model.Colors(col)
        self.typeRules = f.readline().replace("\n", " ").split(" ")
        self.rlDict = eval(f.read())
        
      retVal.append((i, k, col))
      k += 1
    return retVal

  def setLifemapSize(self, width, height):
    ''' '''
    currentLifemap = self.model.getLifeMap()
    currentLifemap._size = tuple(width, height)
  
  def initModel(ruleIndex):
    if self.typeRules[0] == "Moore":
      self.model.ruleManager = RulesNearCells(self.rlDict, True)
    elif .selftypeRules[0] == "vonNeumann":
      self.model.ruleManager = RulesNearCells(self.rlDict, False)
    elif self.typeRules[0] == "margolis":
      self.model.ruleManager = RulesSquares(self.rlDict)

  def setLifeMap(self, lifeMap):
    model.lifeMap = lifeMap