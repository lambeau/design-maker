import unittest

import design_maker.main


class MainTest(unittest.TestCase):

    def test_initialization(self):
        design_maker.main.initialize()

if __name__ == '__main__':
    unittest.main()
