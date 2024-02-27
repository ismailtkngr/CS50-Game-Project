import random
import curses

def snake_game(win):
    curses.curs_set(0)
    win.timeout(100)  # Game speed (in milliseconds)

    up = 0
    left = 1
    down = 2
    right = 3

    snake_direction = right

    snake = [[4, 10], [4, 9], [4, 8]]
    food = [10, 20]

    # Set up the game board with borders
    height, width = win.getmaxyx()
    game_border = [
        [0, 0],
        [0, width-1],
        [height-1, 0],
        [height-1, width-1]
    ]

    win.border()
    win.addch(int(food[0]), int(food[1]), curses.ACS_PI)

    score = 0

    while True:
        key = win.getch()
        if key == ord('q'):
            break

        if key == curses.KEY_UP:
            snake_direction = up
        elif key == curses.KEY_DOWN:
            snake_direction = down
        elif key == curses.KEY_LEFT:
            snake_direction = left
        elif key == curses.KEY_RIGHT:
            snake_direction = right

        new_head = [snake[0][0], snake[0][1]]

        if snake_direction == down:
            new_head[0] += 1
        elif snake_direction == up:
            new_head[0] -= 1
        elif snake_direction == left:
            new_head[1] -= 1
        elif snake_direction == right:
            new_head[1] += 1

        # Check if the snake hit the wall
        if new_head in game_border or new_head in snake:
            break

        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                new_food = [
                    random.randint(1, height-2),
                    random.randint(1, width-2)
                ]
                food = new_food if new_food not in snake else None
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(int(tail[0]), int(tail[1]), ' ')

        win.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

        # Show score
        win.addstr(0, 0, f"Score: {score}")

    win.clear()
    win.addstr(5, 10, f"Game Over - Score: {score}")
    win.addstr(7, 10, "Do you want to play again? (Yes/No)")

    play_again_response = win.getch()
    if play_again_response in [ord('Y'), ord('y')]:
        snake_game(win)

curses.wrapper(snake_game)

   
