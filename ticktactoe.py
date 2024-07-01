import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentplayer = "X"
winner = None
gamerunning = True

# Printing the gameboard
def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

#  Take player input
def playerinput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Oops player is already in that spot.")

# Check for win or tie
def checkhorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True #Return gives the output of the function(Something like a result)
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
# Check row for win or tie
def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True #Return gives the output of the function(Something like a result)
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# Check for diagonal for win or tie
def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True #Return gives the output of the function(Something like a result)
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Check if tie
def checktie(board):
    global gamerunning
    if "-"not in board:
        printboard(board)
        print("Its a tie!")
        gamerunning = False

# Check for win
def checkwin():
    global gamerunning
    if checkdiagonal(board) or checkhorizontle(board) or checkrow(board):
        print(f"The winner is {winner}.")
        gamerunning = False

# Switch player
def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

# Computer
def computer(board):
    while currentplayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchplayer()

# While game is running
while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)

# test







































