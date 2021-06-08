import modules.model.model
from modules.model.rulesNearCells import RulesNearCells
from modules.model.rulesSquares import RulesSquares
import modules.model.lifeMap
import utils.colors
from os import error, listdir
from os.path import isfile, join

class Controller:
  """
    Coltroller is a class that connects Model with View

    Attributes
    ----------
    model: class
        the model that is processed and transfered to view

    Methods
    ----------
    getLifemapSize()
        gets size of models' lifeMap
    getMap()
        gets the lifeMap itself
    getRuleFiles()
        retrieves the files containing rules of the coloring
    initModel(ruleIndex)
        initiates the model with fixed set of rules
    setLifemapSize()
        sets the size of lifeMap
    setLifemap()
        sets lifeMap itself
  """
  
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

  def makeStep(self):
    self.model.makeStep()

  def getRuleFiles(self):
    onlyfiles = [f for f in listdir('./rules') if isfile(join('./rules', f))]
    self.retVal = []
    k = 0
    for i in onlyfiles:
      with open("rules/%s" % i, "r") as f:
        self.col = f.readline().replace("\n", " ").split(" ")
        typeRules = f.readline().replace("\n", " ").split(" ")
        rlDict = eval(f.read())
        
      self.Colors = utils.colors.Colors(self.col)
      self.retVal.append((i, k, self.Colors, typeRules, rlDict))
      k += 1
    return self.retVal

  def setLifemapSize(self, width, height):
    ''' Setting size of models' lifeMap'''

    currentLifemap = self.model.getLifeMap()
    currentLifemap._size = (width, height)
  
  def initModel(self, ruleIndex):
    self.Colors = utils.colors.Colors(self.col)
    for i in self.retVal:
      if i[1] == ruleIndex:
        typeRules = self.retVal[ruleIndex][3]
        rlDict = self.retVal[ruleIndex][4]
        if typeRules[0] == "Moore":
          self.model.ruleManager = RulesNearCells(len(self.col), int(typeRules[1]), True, rlDict)
        elif typeRules[0] == "VonNeumann":
          self.model.ruleManager = RulesNearCells(len(self.col), int(typeRules[1]), False, rlDict)
        elif typeRules[0] == "Margolis":
          self.model.ruleManager = RulesSquares(int(typeRules[1]) if typeRules[1] != "None" else None, rlDict)
        else:
          raise 'Ne zashol!'

  def setCellMatrix(self, cellMatrix):
    self.model.lifeMap.setCellMatrix(cellMatrix)