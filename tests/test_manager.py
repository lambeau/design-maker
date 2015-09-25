import unittest
from unittest import mock

import turtle

mock_turtle = mock.MagicMock()
mock_turtle.count = 0
mock_turtle.setup = mock.create_autospec(turtle.setup)
mock_turtle.Screen = mock.MagicMock()
mock_turtle.Turtle = mock.MagicMock()

from design_maker import manager

class ManagerTest(unittest.TestCase):

    def setUp(self):
        global turtle
        self._turtle = turtle
        turtle = mock_turtle

    def tearDown(self):
        global turtle
        turtle = self._turtle

    def test_singleton(self):
        m1 = manager.Manager()
        m2 = manager.Manager()
        self.assertEqual(m1, m2)

    def test_manager_initializes_turtle_once(self):
        m1 = manager.Manager()
        m2 = manager.Manager()
        self.assertEqual(1, mock_turtle.count)

    def test_state_preservation(self):
        m = manager.Manager()


if __name__ == '__main__':
    unittest.main()
