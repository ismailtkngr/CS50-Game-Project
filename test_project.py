import unittest
from unittest.mock import patch
from io import StringIO
from project import snake_game, main 

class TestSnakeGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['q'])
    def test_game_exit_on_q(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()  

        output = mock_stdout.getvalue().strip()
        self.assertTrue("Game Over" in output)

    @patch('builtins.input', side_effect=['Y', 'q'])
    def test_play_again(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main() 

        output = mock_stdout.getvalue().strip()
        self.assertTrue("Do you want to play again?" in output)
        
    @patch('builtins.input', side_effect=['Y', 'Y', 'Y', 'q'])
    def test_multiple_play_again(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main() 

        output = mock_stdout.getvalue().strip()
        self.assertTrue("Do you want to play again?" in output)

    @patch('builtins.input', side_effect=['a', 'q'])
    def test_invalid_key(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()  

        output = mock_stdout.getvalue().strip()
        self.assertTrue("Game Over" in output)


if __name__ == '__main__':
    unittest.main()
