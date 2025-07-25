import tkinter as tk
from tkinter import messagebox

# Initialize the game grid
def initialize_grid(r, c):
    board = []
    for i in range(r):
        row = [0] * c
        board.append(row)
    return board

# Check for a win condition
def check_win(board, r, player):
    for i in range(len(board)):#horizontal check
        for j in range(len(board[0]) - 3):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    for i in range(len(board[0])):#vertical check
        for j in range(r - 3):
            if board[j][i] == player and board[j+1][i] == player and board[j+2][i] == player and board[j+3][i] == player:
                return True
    for i in range(r - 3):# left down
        for j in range(len(board[0]) - 3):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    for i in range(3, r):#right down
        for j in range(len(board[0]) - 3):
            if board[i][j] == player and board[i-1][j+1] == player and board[i-2][j+2] == player and board[i-3][j+3] == player:
                return True
    return False

# Check for a draw
def check_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

# Drop the disc into the chosen column
def drop_disc(board, r, col, player):
    for i in range(r - 1, -1, -1):
        if board[i][col] == 0:
            board[i][col] = player
            break
    return board

# Switch between players
def switch_player(player):
    return 2 if player == 1 else 1

# Update the board display
def update_board_display():
    for i in range(rows):
        for j in range(cols):
            color = 'white'
            if board[i][j] == 1:
                color = 'red'
            elif board[i][j] == 2:
                color = 'blue'
            canvas.itemconfig(circles[i][j], fill=color)

# Handle column button clicks
def column_click(col):
    global board
    global player

    if not any(board[i][col] == 0 for i in range(rows)):
        messagebox.showinfo("Column Full", "This column is full. Choose another column.")
        return

    board = drop_disc(board, rows, col, player)
    update_board_display()
    if check_win(board, rows, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        root.quit()
    elif check_draw(board):
        messagebox.showinfo("Game Over", "The game is a draw!")
        root.quit()
    player = switch_player(player)

# Set up the Tkinter window
root = tk.Tk()
root.title("Connect Four")

rows = 6
cols = 7
player = 1

# Create the board
board = initialize_grid(rows, cols)

# Create a canvas to draw the board
canvas = tk.Canvas(root, width=700, height=600, bg='skyblue')
canvas.pack()

# Draw the grid and discs
circles = [[canvas.create_oval(j * 100 + 10, i * 100 + 10, j * 100 + 90, i * 100 + 90, fill='white', outline='black') for j in range(cols)] for i in range(rows)]

# Create buttons for each column
for col in range(cols):
    button = tk.Button(root, text=f"Drop in Column {col + 1}", command=lambda c=col: column_click(c))
    button.pack(side=tk.LEFT)

# Start the Tkinter event loop
root.mainloop()
