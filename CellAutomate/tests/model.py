"""Model unit tests module."""
import unittest
from modules.model import Model
from modules.model import LifeMap
from modules.model import RulesNearCells
from modules.model import RulesSquares


class ModelTests(unittest.TestCase):
    """Model unit tests."""

    def test_Moore(self):
        """Moore neighbourhood test."""
        lmZero, lmOne, lmTwo = LifeMap((8, 8)), LifeMap((8, 8)), LifeMap((8, 8))
        lmZero.setCell(2, 3, 1)
        lmZero.setCell(2, 4, 1)
        lmZero.setCell(2, 5, 1)
        lmOne.setCell(1, 4, 1)
        lmOne.setCell(2, 4, 1)
        lmOne.setCell(3, 4, 1)
        lmTwo.setCell(2, 3, 1)
        lmTwo.setCell(2, 4, 1)
        lmTwo.setCell(2, 5, 1)

        model = Model(
            lmZero,
            RulesNearCells(
                2, 0, True, {
                    (0, (5, 3)): 1,
                    (1, (5, 3)): 1,
                    (1, (6, 2)): 1,
                }
            )
        )
        model.makeStep()
        self.assertEqual(model.getLifeMap().getCellMatrix(), lmOne.getCellMatrix())
        model.makeStep()
        self.assertEqual(model.getLifeMap().getCellMatrix(), lmTwo.getCellMatrix())

    def test_Margolis(self):
        """Margolisx neighbourhood test."""
        lmZero, lmOne, lmTwo = LifeMap((8, 8)), LifeMap((8, 8)), LifeMap((8, 8))
        lmZero.setCell(0, 0, 1)
        lmZero.setCell(3, 1, 2)
        lmOne.setCell(0, 0, 2)
        lmOne.setCell(3, 1, 1)
        lmTwo.setCell(0, 0, 1)
        lmTwo.setCell(3, 1, 1)

        model = Model(
            lmZero,
            RulesSquares(
                None, {
                    (1, 0, 0, 0): (2, 0, 0, 0),
                    (0, 2, 0, 0): (0, 1, 0, 0),
                    (0, 0, 1, 0): (0, 0, 2, 0),
                    (0, 0, 0, 2): (0, 0, 0, 1),
                }
            )
        )
        model.makeStep()
        self.assertEqual(model.getLifeMap().getCellMatrix(), lmOne.getCellMatrix())
        model.makeStep()
        self.assertEqual(model.getLifeMap().getCellMatrix(), lmTwo.getCellMatrix())
