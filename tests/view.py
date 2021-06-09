"""View unit tests module."""
import unittest
from unittest.mock import MagicMock
from modules.view import View
from utils.colors import Colors
from tkinter import Canvas


class ViewTests(unittest.TestCase):
    """View unit tests."""

    def setUp(self):
        """Set up tests."""
        controller = MagicMock()
        controller.getLifemapSize = MagicMock(return_value=(50, 50))
        ruleSetup = (
            'GameOfLIfe.txt',
            0,
            Colors(['White', 'Black']),
            ['Moore', '0', ''],
            {(0, (5, 3)): 1, (1, (5, 3)): 1, (1, (6, 2)): 1},
            ['White', 'Black'],
        )
        controller.getRuleFiles = MagicMock(return_value=[ruleSetup])

        self.view = View(controller)

    def test_windowsTransfer(self):
        """Test windows transfer."""
        with self.assertRaises(AttributeError):
            self.view.cvsCells
        self.view.showMainWindow()
        self.assertEqual(type(self.view.cvsCells), Canvas)

    def test_inboundsDraw(self):
        """Inbounds draw test."""
        self.view.controller.getLifemapSize = MagicMock(return_value=(10, 10))
        self.view.showMainWindow()

        i, j = 1, 2
        colorIndex = 0
        obje = self.view.draw(i, j, colorIndex)

        CELL_SIZE = self.view.CELL_SIZE
        x0, y0 = j * CELL_SIZE, i * CELL_SIZE
        x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
        self.assertEqual(self.view.cvsCells.coords(obje), [x0, y0, x1, y1])

    def test_outboundsDraw(self):
        """Outbounds draw test."""
        self.view.controller.getLifemapSize = MagicMock(return_value=(10, 10))
        self.view.showMainWindow()
        object = self.view.draw(10, 10, 0)
        self.assertEqual(object, None)

    def test_inboundsMouseDraw(self):
        """Test mouse draw."""
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
        objectsDiff = [*filter(lambda loc_id: loc_id not in initialObjectIds, currentObjectIds)]
        self.assertTrue(len(objectsDiff) == 1)

        newObjectId = objectsDiff[0]
        newObjectCoords = self.view.cvsCells.coords(newObjectId)
        x0, y0 = j * cellSize, i * cellSize
        x1, y1 = x0 + cellSize, y0 + cellSize
        self.assertEqual(newObjectCoords, [x0, y0, x1, y1])

    def test_outboundsMouseDraw(self):
        """Test mouse draw."""
        self.view.controller.getLifemapSize = MagicMock(return_value=(5, 5))
        self.view.showMainWindow()
        initialObjectIds = self.view.cvsCells.find_all()

        cellSize = self.view.CELL_SIZE
        motionEvent = MagicMock()
        i, j = 5, 5
        motionEvent.x = int(j * cellSize + cellSize // 2)
        motionEvent.y = int(i * cellSize + cellSize // 2)
        self.view.on_CvsCells_HoldingMouseOver(motionEvent)

        currentObjectIds = self.view.cvsCells.find_all()
        objectsDiff = [*filter(lambda loc_id: loc_id not in initialObjectIds, currentObjectIds)]
        self.assertTrue(len(objectsDiff) == 0)
