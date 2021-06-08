import modules.model.model
import modules.model.ruleManager
import modules.model.lifeMap
import utils.colors
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
    self.retVal = []
    for i in onlyfiles:
      k = 0
      with open(i, "r") as f:
        self.col = f.readline().replace("\n", " ").split(" ")
        self.typeRules = f.readline().replace("\n", " ").split(" ")
        self.rlDict = eval(f.read())
        
      self.retVal.append((i, k, col))
      k += 1
    return self.retVal

  def setLifemapSize(self, width, height):
    ''' '''
    currentLifemap = self.model.getLifeMap()
    currentLifemap._size = tuple(width, height)
  
  def initModel(self, ruleIndex):
    self.Colors = utils.colors.Colors(self.col)
    for i in self.retVal:
      if i[0] == ruleIndex:
        if self.typeRules[0] == "Moore":
          self.model.ruleManager = RulesNearCells(len(self.col), int(self.typeRules[1]), True, self.rlDict)
        elif self.typeRules[0] == "vonNeumann":
          self.model.ruleManager = RulesNearCells(len(self.col), int(self.typeRules[1]), False, self.rlDict)
        elif self.typeRules[0] == "margolis":
          self.model.ruleManager = RulesSquares(int(self.typeRules[1]), self.rlDict)

  def setLifeMap(self, lifeMap):
    self.model.lifeMap = lifeMap