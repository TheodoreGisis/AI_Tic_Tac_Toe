import math

class TicTacToe:
#Class constructor 
    def __init__(self):
        self.board = {1:" ", 2:" ",3:" ",
                      4:" ", 5:" ",6:" ",
                      7:" ", 8:" ",9:" "
                        }
        self.player = "X"
        self.Computer ="O"
#Method tha draws the board
    def DrawTheBoard(self):
        print( self.board[1] + "|" + self.board[2] +"|" + self.board[3] )
        print("-----")
        print( self.board[4] + "|" + self.board[5] +"|" + self.board[6] )
        print("-----")
        print( self.board[7] + "|" + self.board[8] +"|" + self.board[9] )
        print("\n")
#Method that checks if the game has a winner
    def CkeckWin(self):

        if(self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1]!=" "):
            return True
        elif(self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4]!=" "):
            return True
        elif(self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7]!=" "):
            return True
        elif(self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1]!=" "):
            return True
        elif(self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2]!=" "):
            return True
        elif(self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3]!=" "):
            return True
        elif(self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1]!=" "):
            return True
        elif(self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7]!=" "):
            return True 
        else:
            return False 
#Method that checks who is the winner
    def CkeckWinMark(self,symbol):
        if(self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] ==symbol):
            return True
        elif(self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4]==symbol):
            return True
        elif(self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7]==symbol):
            return True
        elif(self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1]==symbol):
            return True
        elif(self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2]==symbol):
            return True
        elif(self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3]==symbol):
            return True
        elif(self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1]==symbol):
            return True
        elif(self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7]==symbol):
            return True 
        else:
            return False     
#Merhod that checks if there is a draw
    def CheckDraw(self):
        for i in self.board.keys():
            if self.board[i] == " ":
                return False
        return True
#Method tha finds the empty spaces in the board(" ")
    def FindIfspace(self,position):
        if self.board[position] == ' ':
            return True
        else:
            return False
#Method that inserts the choice of the player-computer in to the board
    def InsertLetterInBoard(self,letter,position):
        if self.FindIfspace(position):
            self.board[position] = letter
            self.DrawTheBoard()
            if self.CkeckWin():    
                if letter == self.Computer:
                    print("Bot won")
                    exit()
                else:
                    print("You won!")
                    exit()
            if self.CheckDraw():
                print("DRAW")
                exit()
        else:
            print("Invalid Position!\n")
            position = int(input("Enter a position"))
            self.InsertLetterInBoard(letter,position)
            return
#Method called when it is player's turn 
    def PlayerTurn(self):
        position = int(input("Give position!"))
        self.InsertLetterInBoard(self.player,position)
        return
#Method called when it is computer's turn   
    def ComputerTurn(self):
        bestscore = -math.inf
        bestmove = None
        for key in self.board.keys():
            if(self.board[key] == " "):
                self.board[key] = self.Computer
                score = self.minimax(self.board,0,False)
                self.board[key] = " "
                if(score > bestscore):
                    bestscore = score
                    bestmove = key
        self.InsertLetterInBoard(self.Computer,bestmove)
#ALGORITHM implementation
    def minimax(self,board, depth, isMaximizing):
        if (self.CkeckWinMark(self.Computer)):
            return 1
        elif (self.CkeckWinMark(self.player)):
            return -1
        elif (self.CheckDraw()):
            return 0

        if (isMaximizing):
            bestScore = -800
            for key in board.keys():
                if (self.board[key] == ' '):
                    self.board[key] = self.Computer
                    score = self.minimax(self.board, depth+1, False)
                    self.board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = 800
            for key in self.board.keys():
                if (self.board[key] == ' '):
                    self.board[key] = self.player
                    score = self.minimax(self.board, depth+1, True)
                    self.board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore
#main
if __name__ == '__main__':
    Tic = TicTacToe()
    Tic.DrawTheBoard()
    print("Computer starts first good luck \n")
    
    while not Tic.CkeckWin():    
        Tic.ComputerTurn()
        Tic.PlayerTurn()
    

    
 
    






