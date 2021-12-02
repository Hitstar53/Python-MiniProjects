'''
TicTacToe Game
'''
import random

def display_board(board):
    '''
    Displays the board after each turn
    '''
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def player_input():
    '''
    Takes player input whether x or o
    '''
    marker = ''
    while marker not in ('X','O'):
        marker = input('Player 1: Do you want to be X or O?\n').upper()
    if marker == 'X':
        return ('X', 'O')
    return ('O', 'X')

def place_marker(board, marker, pos):
    '''
    places marker on the board
    '''
    board[pos] = marker

def win_check(board, mark):
    '''
    Checks if a player has won
    '''
    return ((board[7]==board[8]==board[9]==mark) or
            (board[4]==board[5]==board[6]==mark) or
            (board[1]==board[2]==board[3]==mark) or
            (board[7]==board[4]==board[1]==mark) or
            (board[8]==board[5]==board[2]==mark) or
            (board[9]==board[6]==board[3]==mark) or
            (board[7]==board[5]==board[3]==mark) or
            (board[9]==board[5]==board[1]==mark))

def choose_first():
    '''
    Randomly chooses who goes first
    '''
    if random.randint(1, 2) == 1:
        return 'player1'
    return 'player2'

def space_check(board, pos):
    '''
    Checks if the pos is empty
    '''
    if board[pos] == ' ':
        return True
    return False

def full_board_check(board):
    '''
    Checks if the full board is full or not
    '''
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    '''
    Takes pos input from each player
    '''
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        pos = int(input('Choose your next position: (1-9)\n'))
    return pos

def replay():
    '''
    asks whether player wants to play again or not
    '''
    return input('Do you want to play again? Enter Yes or No:\n').lower().startswith('y')

print('Welcome to Tic Tac Toe!')
while True:
    tttb = [' ']*10
    ply1_mkr, ply2_mkr = player_input()
    TURN = choose_first()
    print(TURN + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.\n')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if TURN == 'player1':
            display_board(tttb)
            position = player_choice(tttb)
            place_marker(tttb, ply1_mkr, position)

            if win_check(tttb, ply1_mkr):
                display_board(tttb)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(tttb):
                    display_board(tttb)
                    print('The game is a draw!')
                    break
                TURN = 'player2'
        else:
            display_board(tttb)
            position = player_choice(tttb)
            place_marker(tttb, ply2_mkr, position)

            if win_check(tttb, ply2_mkr):
                display_board(tttb)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(tttb):
                    display_board(tttb)
                    print('The game is a draw!')
                    break
                TURN = 'player1'
    if not replay():
        break
