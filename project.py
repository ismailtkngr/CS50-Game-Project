import random
import curses

def main():
    curses.wrapper(snake_game)


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

        snake.insert(0, new_head)

        if (
            snake[0][0] == 0
            or snake[0][0] == 23
            or snake[0][1] == 0
            or snake[0][1] == 79
        ):
            break

        if snake[0] in snake[1:]:
            break

        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                new_food = [random.randint(1, 22), random.randint(1, 78)]
                food = new_food if new_food not in snake else None
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(int(tail[0]), int(tail[1]), ' ')

        win.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

        # Check snake size
        if len(snake) > 3:
            # Add a segment to the end of the snake
            win.addch(int(tail[0]), int(tail[1]), curses.ACS_CKBOARD)
            snake.append(tail)

    win.clear()
    win.addstr(5, 10, f"Game Over - Score: {score}")
    win.addstr(7, 10, "Do you want to play again? (Yes/No)")

    play_again_response = win.getch()
    if play_again_response in [ord('Y'), ord('y')]:
        snake_game(win)


if __name__ == "__main__":
    main()



