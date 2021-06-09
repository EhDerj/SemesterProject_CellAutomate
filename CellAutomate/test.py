"""Testing mode launch."""
import sys
sys.path.append('./src')

import unittest
from tests.view import ViewTests
from tests.model import ModelTests

if __name__ == '__main__':
    unittest.main()
