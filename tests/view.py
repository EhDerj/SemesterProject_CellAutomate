import sys
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

  
