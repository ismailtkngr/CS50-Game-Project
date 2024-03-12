import unittest
from unittest.mock import patch
from io import StringIO
import project.py

class TestProject(unittest.TestCase):

    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=['q'])
    def test_game_exit_on_q(self, mock_input):
        project.snake_game()
        output = self.held_output.getvalue().strip()
        self.assertTrue("Game Over" in output)

    @patch('builtins.input', side_effect=['Y', 'q'])
    def test_play_again(self, mock_input):
        project.snake_game()
        output = self.held_output.getvalue().strip()
        self.assertTrue("Do you want to play again?" in output)


if __name__ == '__main__':
    unittest.main()