# Breakout Game

This is a classic Breakout game implemented using the Python Turtle graphics library. The objective of the game is to break all the bricks by bouncing a ball off a paddle.

![Breakout Game](screenshot.png)

## Getting Started

To play the game locally, follow these instructions:

### Prerequisites

- Python 3.11 or higher
- Turtle graphics library (included in Python standard library)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JacobEliks/Breakout-game
   ```

2. Change into the project directory:
   ```bash
   cd breakout-game
   ```

3. run the game:
   ```bash
   python main.py
   ```

# How to Play

Move the paddle using the left and right arrow keys.
Launch the ball by pressing the spacebar.
Try to break all the bricks without letting the ball fall below the paddle.
If the ball falls below the paddle, you lose a life. You have three lives in total.
The game ends when you break all the bricks or lose all your lives.

# Customization

You can customize certain aspects of the game by modifying the following variables in the breakout.py file:

SCREEN_WIDTH: Width of the game window.
SCREEN_HEIGHT: Height of the game window.
PADDLE_WIDTH: Width of the paddle.
PADDLE_HEIGHT: Height of the paddle.
BALL_RADIUS: Radius of the ball.
BRICK_ROWS: Number of rows of bricks.
BRICK_COLUMNS: Number of columns of bricks.
BRICK_WIDTH: Width of each brick.
BRICK_HEIGHT: Height of each brick.
Feel free to experiment with these values to customize the game according to your preferences.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgments

The Breakout game is a classic arcade game popularized by Atari in the 1970s.
This implementation is inspired by various online resources and tutorials.
