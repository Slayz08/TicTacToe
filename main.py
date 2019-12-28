#TIC TAC TOE by Juanelv - 26/12/19

import math
import random

def printBoard(board):
    print("\n")
    print('                    |   |')
    print('                  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('                    |   |')
    print('                 -----------')
    print('                    |   |')
    print('                  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('                    |   |')
    print('                 -----------')
    print('                    |   |')
    print('                  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('                    |   |')
    print("\n")

def choosePlayerLetter(): 
    letter = ""
    while (letter != 'X' and letter != 'O'):
        print("Choose either X or O: ")
        letter = input().upper()

    print("Okay, now you are " + letter + ". Good Luck!")

    if letter == 'X': return ['X', 'O']
    else: return ['O', 'X']

def chooseWhoGoesFirst():
    if random.randint(0, 1) == 0:
        print("Computer goes first") 
        return 'computer'
    else: 
        print("You go first") 
        return 'player'

def askToPlayAgain():
    print("Wanna play another match? (y/n)")
    return input().upper().startswith('Y') #Function returns False if input does not start with Y

def makeMove(board, letter, move):
    board[move] = letter

def checkHorizontal(board, letter):
    return((board[7] == board[8] == board[9] == letter) or
           (board[4] == board[5] == board[6] == letter) or
           (board[1] == board[2] == board[3] == letter))

def checkDiagonal(board, letter):
    return((board[7] == board[5] == board[3] == letter) or
           (board[1] == board[5] == board[9] == letter))

def checkVertical(board, letter):
    return((board[7] == board[4] == board[1] == letter) or
           (board[8] == board[5] == board[2] == letter) or
           (board[9] == board[6] == board[3] == letter))

def checkWinner(board, letter):
    return ( checkHorizontal(board, letter) or checkVertical(board, letter) or checkDiagonal(board, letter) )
    
def theresFreeSpace(board,move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not theresFreeSpace(board, int(move)):
        print("What's your next move? (1 - 9): ")
        move = input()
    return int(move)

def isBoardFull(board):
    for i in range (1, 10):
        if theresFreeSpace(board, i):
            return False
    return True

def getComputerMove(board, computerLetter):

    '''
    #Not AI
    computerMove = random.randint(1,9)
    
    while not theresFreeSpace(board, computerMove):
        computerMove = random.randint(1,9)

    '''

    
    #AI
    bestScore = math.inf
    if computerLetter == "X": 
        maximizing = True
        bestScore = bestScore * -1 
    else: 
        maximizing = False
 
    bestMove = -1

    

    for i in range (1, 10):
        copyBoard = board.copy() 
        if theresFreeSpace(copyBoard, i):
            makeMove(copyBoard, computerLetter, i)
            score = minimax(copyBoard, 0, not (maximizing))   

            if maximizing:
                if score > bestScore:
                    bestScore = max(score, bestScore)
                    bestMove = i
            else: 
                if score < bestScore:
                    bestScore = min(score, bestScore)
                    bestMove = i

    
    return bestMove


# X: +1
# O: -1 
# Tie: 0
def minimax(board, depth, isMaximizing):
    if checkWinner(board, "X"): 
        return 10 - depth
    elif checkWinner(board, "O"): 
        return -1 + depth
    elif isBoardFull(board) and not ( checkWinner(board, "X") or checkWinner(board, "O") ):  return 0


    if isMaximizing:
        bestScore = math.inf * -1
        for i in range (1, 10):
            copyBoard = board.copy()
            if theresFreeSpace(copyBoard, i):
                makeMove(copyBoard, "X", i)
                
                if isBoardFull(copyBoard) : score = minimax(copyBoard, depth+1, False)
                else: score = minimax(copyBoard, depth + 1, False)
                bestScore = max(score, bestScore)
        return bestScore

    else: 
        bestScore = math.inf
        for i in range (1, 10):
            copyBoard = board.copy()
            if theresFreeSpace(copyBoard, i):
                makeMove(copyBoard, "O", i)
                if isBoardFull(copyBoard): score = minimax(copyBoard, depth+1, True)
                else: score = minimax(copyBoard, depth+1, True)
                bestScore = min(score, bestScore)
        return bestScore
                    

    


## Main
print("\n\nWelcome to Tic Tac Toe by Juanelv")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = choosePlayerLetter() #Multiple assignment, first item is playerLetter and second item is computerLetter
    turn = chooseWhoGoesFirst()
    #turn = "player"
    isGamePlaying = True

    while isGamePlaying:

        if turn == 'player':
            printBoard(theBoard)
            move = getPlayerMove(theBoard)
            #move = getComputerMove(theBoard, playerLetter)
            makeMove(theBoard, playerLetter, move)

            if checkWinner(theBoard, playerLetter):
                printBoard(theBoard)
                print("You won! ;)")
                isGamePlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard,computerLetter,move)

            if checkWinner(theBoard, computerLetter):
                printBoard(theBoard)
                print("The computer beat you, what a shame...")
                isGamePlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

    if not askToPlayAgain():
        break
