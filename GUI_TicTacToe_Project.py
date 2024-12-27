import tkinter as tk
from tkinter import messagebox
from random import randrange


wnd = tk.Tk()
wnd.title("TicTacToe")

# Global variables
board = [""] * 9  # Board positions
player = "O"  # User plays 'O'
computer = "X"  # Computer plays 'X'

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Tie"
    return None


def computer_move():
    empty_tiles = [i for i in range(9) if board[i] == ""]
    if empty_tiles:
        move = randrange(len(empty_tiles))
        index = empty_tiles[move]
        board[index] = computer
        buttons[index].config(text=computer, fg="red")
        winner = check_winner()
        if winner:
            end_game(winner)


def player_move(index):
    if board[index] == "":
        board[index] = player
        buttons[index].config(text=player, fg="green")
        winner = check_winner()
        if winner:
            end_game(winner)
        else:
            computer_move()


def end_game(winner):
    if winner == "Tie":
        messagebox.showinfo("Game Over", "It's a Tie!")
    else:
        messagebox.showinfo("Game Over", f"{winner} won!")
    wnd.destroy()  # Close the game window

# Create the game buttons
buttons = []
for i in range(9):
    button = tk.Button(wnd, text="", font=("Arial", 24), height=2, width=5,
                       command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Computer makes the first move
board[4] = computer
buttons[4].config(text=computer, fg="red")


wnd.mainloop()
