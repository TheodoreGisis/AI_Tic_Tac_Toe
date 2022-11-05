# AI_Tic_Tac_Toe

## Description 
This is a simple Tic-Tac-Toe game created in Python. But is it so simple as it looks? To be honest, this is a Tic-Tac-Toe game using Artificial Intelligence and to be more specific we used the MiniMax algorithm. To beat the computer (or at least try), you need to make use of a bit of strategy. Strategy means figuring out what you need to do to win. Part of your strategy is trying to figure out how to get three 'X' in a row. The other part is trying to figure out how to stop the computer from getting three 'O' in a row. After you put an 'X' in a square, you start looking ahead. Where's the best place for your next X? You look at the empty squares and decide which ones are good choices—which ones might let you make three 'X' in a row. You also have to watch where the computer puts its 'O'. That could change what you do next. If the computer gets two 'O' in a row, you have to put your next X in the last empty square in that row, or the computer will win. You are forced to play in a particular square or lose the game.

If you always pay attention and look ahead, you'll never lose a game of Tic-Tac-Toe. You may not win, but at least you'll tie.

## What is MiniMax algorithm?

The min max or minimax algorithm, is a popular AI algorithm, and it used in decision-making, game theory and artificial intelligence(AI).Usually we use minimax in two player games such as tic-tac-toe, chess and go. Basically, as we can see from the name of the algorithm, this is a recursive program written to find the best gameplay that minimizes any tendency to lose a game while maximizing any opportunity to win the game.

## How it works?
The algorithm search, recursively, the best move that leads the Max player to win or not lose (draw). It consider the current state of the game and the available moves at that state, then for each valid move it plays (alternating min and max) until it finds a terminal state (win, draw or lose).

## How to play

TicTacToeAI.PY file is the one that you need to run, if you want to start the game. The rules of the game are simple, you are playing against the computer. Your letter is 'O' and computer's letter is 'X'. Be careful because you are playing against an AI robot, so it will be a challenge for you to win....if you can.
