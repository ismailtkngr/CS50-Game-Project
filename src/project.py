import random
import curses

def main():
    curses.wrapper(run_game)

def run_game(win):
    curses.curs_set(0)
    win.timeout(100)  # Game speed

    UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
    snake_direction = RIGHT

    snake = [[4, 10], [4, 9], [4, 8]]
    food = [10, 20]

    height, width = win.getmaxyx()
    game_border = create_border(height, width)

    win.border()
    draw_food(win, food)

    score = 0

    while True:
        key = win.getch()
        if key == ord('q'):
            break

        snake_direction = get_snake_direction(key, snake_direction, UP, DOWN, LEFT, RIGHT)

        new_head = calculate_new_head(snake[0], snake_direction)

        if is_collision(new_head, game_border) or is_collision(new_head, snake):
            break

        snake.insert(0, new_head)

        score, food = update_score_and_food(win, snake[0], food, snake, height, width, score)

        draw_snake(win, snake)
        draw_score(win, score)

    end_game(win, score)

def create_border(height, width):
    return [
        [0, 0],
        [0, width-1],
        [height-1, 0],
        [height-1, width-1]
    ]

def draw_food(win, food):
    win.addch(int(food[0]), int(food[1]), curses.ACS_PI)

def get_snake_direction(key, current_direction, UP, DOWN, LEFT, RIGHT):
    if key == curses.KEY_UP:
        return UP if current_direction != DOWN else current_direction
    elif key == curses.KEY_DOWN:
        return DOWN if current_direction != UP else current_direction
    elif key == curses.KEY_LEFT:
        return LEFT if current_direction != RIGHT else current_direction
    elif key == curses.KEY_RIGHT:
        return RIGHT if current_direction != LEFT else current_direction
    return current_direction

def calculate_new_head(current_head, direction):
    new_head = current_head[:]
    if direction == 0:
        new_head[0] -= 1
    elif direction == 1:
        new_head[1] -= 1
    elif direction == 2:
        new_head[0] += 1
    elif direction == 3:
        new_head[1] += 1
    return new_head

def is_collision(item, items):
    return item in items

def update_score_and_food(win, head, food, snake, height, width, score):
    if head == food:
        score += 1
        food = generate_food(height, width, snake)
        draw_food(win, food)
    else:
        tail = snake.pop()
        win.addch(int(tail[0]), int(tail[1]), ' ')
    return score, food

def draw_snake(win, snake):
    win.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

def draw_score(win, score):
    win.addstr(0, 0, f"Score: {score}")

def generate_food(height, width, snake):
    food = None
    while food is None:
        new_food = [
            random.randint(1, height-2),
            random.randint(1, width-2)
        ]
        food = new_food if new_food not in snake else None
    return food

def end_game(win, score):
    win.clear()
    win.addstr(5, 10, f"Game Over - Score: {score}")
    win.addstr(7, 10, "Do you want to play again? (Yes/No)")

    play_again_response = win.getch()
    if play_again_response in [ord('Y'), ord('y')]:
        run_game(win)

if __name__ == "__main__":
    main()
