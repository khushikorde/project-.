import math

def print_board(board):
    for row in board:
        print(row)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def empty_cells(board):
    return [(i,j) for i in range(3) for j in range(3) if board[i][j]==" "]

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if not empty_cells(board): return 0

    if is_max:
        best = -math.inf
        for (i,j) in empty_cells(board):
            board[i][j] = "O"
            best = max(best, minimax(board, depth+1, False))
            board[i][j] = " "
        return best
    else:
        best = math.inf
        for (i,j) in empty_cells(board):
            board[i][j] = "X"
            best = min(best, minimax(board, depth+1, True))
            board[i][j] = " "
        return best

def best_move(board):
    move = None
    best = -math.inf
    for (i,j) in empty_cells(board):
        board[i][j] = "O"
        score = minimax(board,0,False)
        board[i][j] = " "
        if score > best:
            best = score
            move = (i,j)
    return move

board = [[" "]*3 for _ in range(3)]
while True:
    print_board(board)
    if check_winner(board) or not empty_cells(board):
        print("Game Over! Winner:", check_winner(board))
        break

    x,y = map(int,input("Enter your move (row col): ").split())
    if board[x][y] == " ":
        board[x][y] = "X"
    else:
        print("Invalid move!")
        continue

    if not empty_cells(board): break
    move = best_move(board)
    board[move[0]][move[1]] = "O"