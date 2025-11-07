# Simple Tic Tac Toe with Minimax

def print_board(b):
    for i in range(0, 9, 3):
        print(b[i], b[i+1], b[i+2])
    print()

def winner(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[x]==b[y]==b[z]==p for x,y,z in wins)

def minimax(b, is_max):
    if winner(b,"O"): return 1
    if winner(b,"X"): return -1
    if " " not in b: return 0

    if is_max:  # computer turn
        best = -2
        for i in range(9):
            if b[i]==" ":
                b[i]="O"
                best = max(best, minimax(b, False))
                b[i]=" "
        return best
    else:       # player turn
        best = 2
        for i in range(9):
            if b[i]==" ":
                b[i]="X"
                best = min(best, minimax(b, True))
                b[i]=" "
        return best

def best_move(b):
    best, move = -2, -1
    for i in range(9):
        if b[i]==" ":
            b[i]="O"
            score = minimax(b, False)
            b[i]=" "
            if score > best:
                best, move = score, i
    return move

# Main game
board = [" "]*9
print("You are X, computer is O (enter 0-8):")
print_board(board)

while True:
    # Player
    p = int(input("Your move: "))
    if board[p]!=" ":
        print("Invalid!"); continue
    board[p]="X"
    print_board(board)
    if winner(board,"X"): print("You win!"); break
    if " " not in board: print("Draw!"); break

    # Computer
    c = best_move(board)
    board[c]="O"
    print("Computer:", c)
    print_board(board)
    if winner(board,"O"): print("Computer wins!"); break
    if " " not in board: print("Draw!"); break


"""
OUTPUT 
You are X, computer is O (enter 0-8):
     
     
     

Your move: 0
X    
     
     

Computer: 4
X
  O


Your move: 1
X X  
  O


Computer: 2
X X O
  O
     

Your move: 3
X X O
X O


Computer: 6
X X O
X O
O

Computer wins!


EXPLANATION 
🧩 1. print_board(b)
def print_board(b):
    for i in range(0, 9, 3):
        print(b[i], b[i+1], b[i+2])
    print()


Prints the 3×3 Tic Tac Toe board.

The board b is a list of 9 items ("X", "O", or " ").

It prints 3 symbols per line (0–2, 3–5, 6–8).

The last print() just adds a blank line for spacing.

🏆 2. winner(b, p)
def winner(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(b[x]==b[y]==b[z]==p for x,y,z in wins)


Defines all 8 possible winning lines (rows, columns, diagonals).

Checks if all three positions in any line have the same symbol p.

Returns True if that player wins, else False.

🧠 3. minimax(b, is_max)
def minimax(b, is_max):
    if winner(b,"O"): return 1
    if winner(b,"X"): return -1
    if " " not in b: return 0


This is the AI’s decision-making function.

Base cases:

If O (computer) wins → score +1

If X (player) wins → score -1

If no empty spaces → score 0 (draw)

🤖 4. Computer’s turn (maximize score)
    if is_max:
        best = -2
        for i in range(9):
            if b[i]==" ":
                b[i]="O"
                best = max(best, minimax(b, False))
                b[i]=" "
        return best


When it’s the computer’s turn, it tries all empty spots.

It places "O" temporarily and calls minimax again assuming the next turn is the player’s (False).

After checking, it undoes the move (b[i] = " ").

Keeps the highest score (best move for computer).

🧍‍♂️ 5. Player’s turn (minimize score)
    else:
        best = 2
        for i in range(9):
            if b[i]==" ":
                b[i]="X"
                best = min(best, minimax(b, True))
                b[i]=" "
        return best


When it’s the player’s turn, it also tries all empty spots.

It assumes the player will play optimally to minimize the computer’s score.

Keeps the lowest score (worst for computer, best for player).

🎯 6. Finding the best move
def best_move(b):
    best, move = -2, -1
    for i in range(9):
        if b[i]==" ":
            b[i]="O"
            score = minimax(b, False)
            b[i]=" "
            if score > best:
                best, move = score, i
    return move


Loops through all empty spots.

For each possible computer move, calls minimax to get its score.

Chooses the move with the highest score.

🕹️ 7. Main game loop
board = [" "]*9
print("You are X, computer is O (enter 0-8):")
print_board(board)


Creates an empty board of 9 spaces.

Displays instructions and the empty grid.

👤 Player’s move
p = int(input("Your move: "))
if board[p]!=" ":
    print("Invalid!"); continue
board[p]="X"
print_board(board)
if winner(board,"X"): print("You win!"); break
if " " not in board: print("Draw!"); break


Asks for player input (0–8).

Checks if the chosen cell is free.

Places "X" and prints the board.

Checks if the player has won or if it’s a draw.

💻 Computer’s move
c = best_move(board)
board[c]="O"
print("Computer:", c)
print_board(board)
if winner(board,"O"): print("Computer wins!"); break
if " " not in board: print("Draw!"); break


Calls best_move() to pick the best possible spot.

Places "O" there and prints the board.

Checks for win or draw again.

🏁 Example Game Output
You are X, computer is O (enter 0-8):

Your move: 0
X
Computer: 4
X   O
Your move: 1
X X
Computer: 2
X X O
Computer: 6
Computer wins!
"""