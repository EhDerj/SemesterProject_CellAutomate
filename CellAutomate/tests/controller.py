"""Controller unit tests module."""
from logging import makeLogRecord
import unittest
from unittest.mock import MagicMock
from modules.controller import Controller

class ControllerTests(unittest.TestCase):
    """Controller unit tests."""

    def setUp(self):
        model = MagicMock()
        self.model = model
        self.controller = Controller(model)

    def test_makeStep(self):
        def makeStep():
          self.model.isStepMade = True

        self.model.isStepMade = False
        self.model.makeStep = makeStep
        self.controller.makeStep()
        self.assertTrue(self.model.isStepMade)

    def test_makeStep(self):
        def makeStep():
          self.model.isStepMade = True

        self.model.isStepMade = False
        self.model.makeStep = makeStep
        self.controller.makeStep()
        self.assertTrue(self.model.isStepMade)

    def test_getLifeMap(self):
        checkValue = 132132
        self.model.getLifeMap = MagicMock(return_value=checkValue)
        lifeMap = self.controller.getMap()
        self.assertEqual(lifeMap, checkValue)
