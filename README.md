# AI_Tic_Tac_Toe

## What is MiniMax algorithm?

The min max or minimax algorithm, is a popular AI algorithm, and it used in decision-making, game theory and artificial intelligence(AI).Usually we use minimax in two player games such as tic-tac-toe, chess and go. Basically, as we can see from the name of the algorithm, this is a recursive program written to find the best gameplay that minimizes any tendency to lose a game while maximizing any opportunity to win the game.

## How it works?
The algorithm search, recursively, the best move that leads the Max player to win or not lose (draw). It consider the current state of the game and the available moves at that state, then for each valid move it plays (alternating min and max) until it finds a terminal state (win, draw or lose).
