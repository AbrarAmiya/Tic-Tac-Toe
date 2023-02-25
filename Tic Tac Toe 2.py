import tkinter as tk
from PIL import Image, ImageTk
class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Initialize the game board
        self.board = [' ' for _ in range(9)]



        # Load the background image
        self.bg_image = tk.PhotoImage(file="Images/hh.png")

        # Create the background label
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create the game board GUI
        self.create_board()

        # Initialize the player
        self.current_player = 'X'

    def create_board(self):
        # Create the cells
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell_frame = tk.Frame(self.master, width=100, height=100, bd=2, relief="sunken")
                cell_frame.grid(row=i, column=j)
                cell_frame.pack_propagate(0)
                img = Image.open("images/doggy.png")
                img = img.resize((80, 80), Image.ANTIALIAS)
                my_image = ImageTk.PhotoImage(img)




                # cell_button = tk.Button(cell_frame,text="", font=("Helvetica", 50),  command=lambda row=i, col=j: self.make_move(row, col))
               # cell_button = tk.Button(cell_frame, text="", font=("Helvetica", 50), image=my_image, command=lambda row=i, col=j: self.make_move(row, col))
               #  cell_button = tk.Button(cell_frame, text="", font=("Helvetica", 50), image=my_image, fg='blue',
               #                          command=lambda row=i, col=j: self.make_move(row, col))
                cell_button = tk.Button(cell_frame, text="", font=("Helvetica", 50), fg='black', image=my_image, compound="center", command=lambda row=i, col=j: self.make_move(row, col))


                cell_button.image = my_image  # keep a reference to prevent garbage collection

                cell_button.pack(fill=tk.BOTH, expand=True)
                row.append(cell_button)
            self.cells.append(row)

    def make_move(self, row, col):
        # Check if the cell is already taken
        if self.cells[row][col]['text'] != "":
            return

        # Update the game board and the GUI
        self.cells[row][col].configure(text=self.current_player)
        self.board[3 * row + col] = self.current_player

        # Check if the game is over
        winner = self.check_winner()
        if winner is not None:
            self.show_winner(winner)
            for row in self.cells:
                for cell in row:
                    cell.configure(state="disabled")
            return

        if ' ' not in self.board:
            self.show_winner(None)
            return

        # Switch to the other player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i:i+3] == ['X', 'X', 'X']:
                return 'X'
            elif self.board[i:i+3] == ['O', 'O', 'O']:
                return 'O'

        # Check columns
        for i in range(3):
            if self.board[i::3] == ['X', 'X', 'X']:
                return 'X'
            elif self.board[i::3] == ['O', 'O', 'O']:
                return 'O'

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ':
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ':
            return self.board[2]

        return None

    def show_winner(self, winner):
        for row in self.cells:
            for cell in row:
                cell.configure(state="disabled")
        if winner is None:
            message = "It's a tie!"
        else:
            message = f"{winner} wins!"
        self.game_over = tk.Label(self.master, text=message, font=("Helvetica", 25))
        self.game_over.pack()

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()