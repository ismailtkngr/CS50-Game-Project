# SIMPLE SNAKE GAME

#### Video Demo:  <https://www.youtube.com/watch?v=6Y1F_yjUotg>
#### Description:

This was my final project for conclude the course CS50P Introduction to Programming with Python.

This project is a simple implementation of the classic Snake Game using Python's curses library. The game allows the player to control a snake, eat food, and grow in size while avoiding collisions with the walls and the snake's own body.

## Features

- Snake movement in four directions (up, down, left, right).
- Randomly generated food for the snake to eat.
- Game over conditions when the snake collides with the walls or itself.
- Score tracking.

## Project Structure

The project consists of the following files:

- `project.py`: The main Python script containing the game logic.
- `README.md`: This file, providing an overview of the project.
- `test_project.py`: Directory containing test scripts for the project.

## Explaining My Coding

### main():
This function is the entry point of your program. It sets up the curses environment by wrapping the run_game function within the curses.wrapper() function. This ensures that the curses environment is properly initialized and cleaned up.

### run_game(win):
This function is the core of your game. It runs the main game loop where the snake moves, the player interacts with the game, and the game state is updated accordingly. It handles keyboard input, updates the snake's position, checks for collisions, updates the score, draws the snake and the food, and handles the end of the game.

### create_border(height, width):
This function creates the border of the game screen. It returns a list containing the coordinates of the corners of the game screen, which is used to detect collisions with the border.

### draw_food(win, food):
This function draws the food on the game screen. It takes the window (win) and the coordinates of the food (food) as arguments and uses the curses.addch() function to draw the food symbol on the screen.

### get_snake_direction(key, current_direction, UP, DOWN, LEFT, RIGHT):
This function determines the direction in which the snake should move based on the player's keyboard input. It takes the pressed key, the current direction of the snake, and constants representing the directions (UP, DOWN, LEFT, RIGHT) as arguments and returns the new direction of the snake.

### calculate_new_head(current_head, direction):
This function calculates the new head position of the snake based on its current head position and the direction in which it is moving.

### is_collision(item, items):
This function checks if a collision has occurred between the snake and an item (either the game border or itself). It returns True if there is a collision, and False otherwise.

### update_score_and_food(win, head, food, snake, height, width, score):
This function updates the score and the position of the food when the snake eats it. It also handles the removal of the snake's tail when it moves.

### draw_snake(win, snake):
This function draws the snake on the game screen. It takes the window (win) and the coordinates of the snake (snake) as arguments and uses the curses.addch() function to draw the snake symbol on the screen.

### draw_score(win, score):
This function draws the score on the game screen. It takes the window (win) and the current score (score) as arguments and uses the curses.addstr() function to draw the score text on the screen.

### generate_food(height, width, snake):
This function generates random coordinates for the food on the game screen. It ensures that the food does not overlap with the snake's body.

### end_game(win, score):
This function handles the end of the game. It clears the game screen, displays the final score, and prompts the player to play again if they choose to. If the player decides to play again, the run_game() function is called again.

Overall, these functions work together to create a simple snake game using the curses module in Python.

## Usage

To play the game, run the `project.py` script. Use the arrow keys to control the snake's direction. Press 'q' to quit the game.


## Testing
The project includes a testing suite using the pytest framework. To run the tests, use the following command:

`pytest test_project.py`

## Dependencies
The project relies on the following Python libraries:

curses: Used for creating a terminal-based user interface.  
random: Utilized for generating random positions for the food.

### About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.


