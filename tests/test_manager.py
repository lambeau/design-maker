import unittest
from unittest.mock import patch, MagicMock

from design_maker import manager

class ManagerTest(unittest.TestCase):

    def setUp(self):
        manager.Manager.__instance = None

    def test_singleton(self):
        m1 = manager.Manager()
        m2 = manager.Manager()
        self.assertIs(m1, m2)

    @patch('design_maker.manager.turtle')
    def test_manager_initializes_turtle_once(self, mock_turtle):
        m1 = manager.Manager()
        m2 = manager.Manager()
        self.assertEqual(1, mock_turtle.setup.call_count)

    def test_zmock_leak(self):
        self.assertFalse(isinstance(manager.Manager().pen, MagicMock))

    def test_state_preservation(self):
        m1 = manager.Manager()
        start_state = m1.get_state()
        m1.forward(50)
        m1.left(100)
        end_state = m1.get_state()
        m2 = manager.Manager()
        m1.reset()
        self.assertEqual(start_state, m1.get_state())
        self.assertEqual(end_state, m2.get_state())
        self.assertNotEqual(start_state, m2.get_state())


if __name__ == '__main__':
    unittest.main()
