#!python3

"""
TIC TAC TOE
x.o
.x.
.xo
Input number for where you want your piece
                123
                456
                789
"""
board = ["empty",".",".",".",".",".",".",".",".","."]

def dis():
    print(board[1] + board[2] + board[3] + "\n" + board[4] + board[5] + board[6] + "\n" + board[7] + board[8] + board[9])

def xTurn():
    x = int(input("X turn: "))
    if  x > 0 and x < 10 and board[x] == ".":
        board[x] = "X"
        dis()
        if check("X") == False:
            yTurn()
    else:
        print("Invalid space")
        xTurn()

def yTurn():
    y = int(input("Y turn: "))
    if  y > 0 and y < 10 and board[y] == ".":
        board[y] = "O"
        dis()
        if check("O") == False:
            xTurn()
    else:
        print("Invalid space")
        yTurn()

def win(winner):
    print("Game over")
    print(winner + " won the game!")

def check(n):
    if board[1] == n and board[2] == n and board[3] == n:
        win(n)
        return True
    elif board[4] == n and board[5] == n and board[6] == n:
        win(n)
        return True
    elif board[7] == n and board[8] == n and board[9] == n:
        win(n)
        return True
    elif board[1] == n and board[4] == n and board[7] == n:
        win(n)
        return True
    elif board[2] == n and board[5] == n and board[8] == n:
        win(n)
        return True
    elif board[3] == n and board[6] == n and board[9] == n:
        win(n)
        return True
    elif board[1] == n and board[5] == n and board[9] == n:
        win(n)
        return True
    elif board[3] == n and board[5] == n and board[7] == n:
        win(n)
        return True
    elif "." not in board:
        win("Nobody")
        return True
    else:
        return False

dis()
xTurn()