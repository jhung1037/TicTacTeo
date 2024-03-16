# Tic Tac Toe

A clean terminal interface Tic Tac Toe game where you can play against your friend or the computer, or even watch the computer playing against itself!

## Unbeatable AI Feature
- Access through the "Computer" option with the level set to "hard".
- Powered by a recursive structured minimax algorithm.
- Anticipates the best move of the opponent to calculate the optimal move for itself.

## Optimized Minimax Algorithm

### Discovery:
The unbeatable AI prioritizes avoiding "Draw" circumstances. Consequently, its move selection may differ from human intuition.

### Example:
1. Humans often start with the middle square, but the minimax algorithm may begin with corner squares to avoid the inevitable "Draw" outcome.
2. Humans usually won't go with the most upper left square in this case; however, the minimax algorithm suggested there is no difference.
     |   |            O |   |
   - + - + -          - + - + -
     | O |      ->      | O |   
   - + - + -          - + - + -
     |   | X            |   | X

### Optimization:
- Introduced the sum_score variable to calculate the best overall score of possibility once two or more squares were seen as having the same winning possibility.
- Based on the sum_score returned to the very top, the corner squares and the middle square have the same value. Thus, the Unbeatable AI's first move was set to randomly choose from these squares to save time.
