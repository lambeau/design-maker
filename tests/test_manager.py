import unittest
from unittest.mock import patch, MagicMock

from design_maker import manager

class ManagerTest(unittest.TestCase):

    def setUp(self):
        manager.Manager._instance = None

    def test_singleton(self):
        m1 = manager.Manager()
        m2 = manager.Manager()
        self.assertIs(m1, m2)

    @patch('design_maker.manager.turtle')
    def test_manager_initializes_turtle_once(self, mock_turtle):
        m1 = manager.Manager()
        m2 = manager.Manager()
        self.assertEqual(1, mock_turtle.setup.call_count)

    def test_state_preservation(self):
        m1 = manager.Manager()
        start_state = m1.get_state()
        with m1 as temp_manager:
            temp_manager.forward(50)
            self.assertNotEqual(start_state, m1.get_state())
        self.assertEqual(start_state, m1.get_state())


if __name__ == '__main__':
    unittest.main()
