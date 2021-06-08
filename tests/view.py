import sys
from unittest.signals import registerResult
sys.path.append('../src')

import unittest
from unittest.mock import MagicMock
from modules.view import View

class ViewTests(unittest.TestCase):
  def setUp(self):
    controller = MagicMock()
    controller.getLifemapSize = MagicMock(return_value=(50, 50))

    self.view = View(controller)

  def test_draw(self):
    self.view.showMainWindow()
    object = self.view.draw(0, 0, 0)
    print(self.view.cvsCells.itemconfig(object))
