"""Controller unit tests module."""
import unittest
from unittest.mock import MagicMock
from modules.controller import Controller


class ControllerTests(unittest.TestCase):
    """Controller unit tests."""

    def setUp(self):
        """Set up controller tests."""
        model = MagicMock()
        self.model = model
        self.controller = Controller(model)

    def test_makeStep(self):
        """Test make step."""
        def makeStep():
            self.model.isStepMade = True

        self.model.isStepMade = False
        self.model.makeStep = makeStep
        self.controller.makeStep()
        self.assertTrue(self.model.isStepMade)

    def test_getLifeMap(self):
        """Test life map."""
        checkValue = 132132
        self.model.getLifeMap = MagicMock(return_value=checkValue)
        lifeMap = self.controller.getMap()
        self.assertEqual(lifeMap, checkValue)

    def test_getLifeMapSize(self):
        """Test life map size."""
        checkValue = 132132
        lifeMap = MagicMock()
        lifeMap.getSize = MagicMock(return_value=checkValue)
        self.model.getLifeMap = MagicMock(return_value=lifeMap)
        lifeMap = self.controller.getLifemapSize()
        self.assertEqual(lifeMap, checkValue)
