# Tic Tac Toe

A clean terminal interface Tic Tac Toe game where you can play against your friend or the computer, or even watch the computer playing against itself!

## Unbeatable AI Feature
- Access through the "Computer" option with the level set to "hard".
- Powered by a recursive structured minimax algorithm.
- Anticipates the best move of the opponent to calculate the optimal move for itself.

## Optimized Minimax Algorithm

### Discovery:
The unbeatable AI tends to select any available squares since the game consistently results in a "Draw" outcome when both players make the most optimal moves based on the minimax algorithm. Consequently, its move selection may differ from human intuition.

### Example:
1. Humans often start with the middle square, but the AI may begin with corner squares.
2. Humans usually won't go with the most upper left square in the illustrated case; however, the AI considered there is no difference.
<pre>
     |   |           O |   |
   - + - + -         - + - + -
     | O |      ->     | O |   
   - + - + -         - + - + -
     |   | X           |   | X
</pre>

### Optimization:
- Introduced the 'sum_score' variable to calculate the best overall score of all the future possible outcomes once two or more squares were seen as having the same winning possibility.
- Based on the 'sum_score' returned to the very top, the corner squares and the middle square have the same value. Thus, the Unbeatable AI's first move was set to randomly choose from these squares to save time.
