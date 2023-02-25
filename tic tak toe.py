# Tic Tac Toe game in Python

def draw_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def tic_tac_toe():
    board = [' ' for i in range(9)]
    player = 'X'
    while True:
        draw_board(board)
        move = input("It's " + player + "'s turn. Enter a position (1-9): ")
        move = int(move) - 1
        if board[move] == ' ':
            board[move] = player
            if check_win(board, player):
                print(player + ' wins!')
                return
            player = 'O' if player == 'X' else 'X'
        else:
            print('That position is already taken.')

tic_tac_toe()
