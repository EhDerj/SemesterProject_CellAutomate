import sys
from typing import Match
from unittest.signals import registerResult
sys.path.append('../src')

import unittest
from unittest.mock import MagicMock
from modules.view import View

class ViewTests(unittest.TestCase):

  def setUp(self):
    '''Setup tests'''
    controller = MagicMock()
    controller.getLifemapSize = MagicMock(return_value=(50, 50))

    self.view = View(controller)

  def test_inboundsDraw(self):
    '''Inbounds draw test'''
    self.view.controller.getLifemapSize = MagicMock(return_value=(10, 10))
    self.view.showMainWindow()

    i, j = 1, 2
    colorIndex = 0
    object = self.view.draw(i, j, colorIndex)

    CELL_SIZE = self.view.CELL_SIZE
    x0, y0 = j * CELL_SIZE, i * CELL_SIZE
    x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
    self.assertEqual(self.view.cvsCells.coords(object), [x0, y0, x1, y1])
    
  def test_outboundsDraw(self):
    '''Outbounds draw test'''
    self.view.controller.getLifemapSize = MagicMock(return_value=(10, 10))
    self.view.showMainWindow()
    object = self.view.draw(10, 10, 0)
    self.assertEqual(object, None)

  def test_inboundsMouseDraw(self):
    '''Tests mouse draw'''
    self.view.controller.getLifemapSize = MagicMock(return_value=(5, 5))
    self.view.showMainWindow()
    initialObjectIds = self.view.cvsCells.find_all()

    cellSize = self.view.CELL_SIZE
    motionEvent = MagicMock()
    i, j = 0, 4
    motionEvent.x = int(j * cellSize + cellSize // 2)
    motionEvent.y = int(i * cellSize + cellSize // 2)
    self.view.on_CvsCells_HoldingMouseOver(motionEvent)

    currentObjectIds = self.view.cvsCells.find_all()
    objectsDiff = [*filter(lambda id: id not in initialObjectIds, currentObjectIds)]
    self.assertTrue(len(objectsDiff) == 1)

    newObjectId = objectsDiff[0]
    newObjectCoords = self.view.cvsCells.coords(newObjectId)
    print(newObjectCoords)
    x0, y0 = j * cellSize, i * cellSize
    x1, y1 = x0 + cellSize, y0 + cellSize
    self.assertEqual(newObjectCoords, [x0, y0, x1, y1])
  
