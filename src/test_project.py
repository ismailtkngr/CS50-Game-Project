import unittest
import curses
from unittest.mock import patch
from test import create_border, get_snake_direction, calculate_new_head, is_collision, main

class TestSnakeGameFunctions(unittest.TestCase):

    @patch("curses.wrapper")
    def test_main(self, mock_wrapper):
        main()
        mock_wrapper.assert_called_once()

    def test_create_border(self):
        height, width = 10, 20
        expected_border = [
            [0, 0],
            [0, width-1],
            [height-1, 0],
            [height-1, width-1]
        ]
        self.assertEqual(create_border(height, width), expected_border)


    def test_get_snake_direction(self):
        self.assertEqual(get_snake_direction(curses.KEY_UP, 1, 0, 2, 3, 4), 0)
        self.assertEqual(get_snake_direction(curses.KEY_DOWN, 2, 0, 2, 3, 4), 2)
        self.assertEqual(get_snake_direction(curses.KEY_LEFT, 3, 0, 2, 3, 4), 3)
        self.assertEqual(get_snake_direction(curses.KEY_RIGHT, 4, 0, 2, 3, 4), 4)

    def test_calculate_new_head(self):
        self.assertEqual(calculate_new_head([3, 5], 0), [2, 5])
        self.assertEqual(calculate_new_head([3, 5], 1), [3, 4])
        self.assertEqual(calculate_new_head([3, 5], 2), [4, 5])
        self.assertEqual(calculate_new_head([3, 5], 3), [3, 6])

    def test_is_collision(self):
        self.assertTrue(is_collision([2, 3], [[1, 2], [2, 3], [3, 4]]))
        self.assertFalse(is_collision([5, 6], [[1, 2], [2, 3], [3, 4]]))

if __name__ == '__main__':
    unittest.main()
