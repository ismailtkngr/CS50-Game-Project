# Snake Game Project

## Overview

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

## Usage

To play the game, run the `project.py` script. Use the arrow keys to control the snake's direction. Press 'q' to quit the game.


## Testing
The project includes a testing suite using the pytest framework. To run the tests, use the following command:

bash
Copy code
pytest tests/

## Dependencies
The project relies on the following Python libraries:

curses: Used for creating a terminal-based user interface.
random: Utilized for generating random positions for the food.

## Contributing
Feel free to contribute to the project by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

```bash
python project.py
