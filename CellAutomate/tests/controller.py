"""Controller unit tests module."""
import unittest
from unittest.mock import MagicMock
from modules.controller import Controller

class ControllerTests(unittest.TestCase):
    """Controller unit tests."""

    def setUp(self):
      model = MagicMock()

      self.model = model
      #self.controller = Controller(model)


