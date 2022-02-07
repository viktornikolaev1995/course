"""Reverse Tic-Tac-Toe game"""
from copy import copy
import random
import re


play_board = ['| - |' if num % 2 else '-' for num in range(1, 101)]
play_board_idx = {idx for idx, i in enumerate(play_board)}
players_marks = ['X', 'O']
n = 10  # quantity of horizontal and vertical labels


def chunks(lst, n):
    """Yield successive n-sized chunks from lst"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def display_board(board_list):
    """Prints the game board"""
    board_list_reversed = [i for i in reversed(board_list)]
    vert_label_count = n - 1
    horiz_label_count = n - 1
    horiz_labels = ''
    for i in range(n):
        horiz_labels += f'\t{horiz_label_count}'
        horiz_label_count -= 1
    print(horiz_labels)

    for i in list(chunks(board_list_reversed, n)):
        if vert_label_count == n:
            print(vert_label_count, end="  ")
        else:
            print(vert_label_count, end="   ")
        print(*i)
        vert_label_count -= 1


def player_input():
    """Gets a player input string to choose the game mark to play and automatically determines a computer mark"""
    player = ''
    while player not in ('X', 'O'):
        player = input('Player, please choose your marker: X or O: ').upper()
    if player == 'X':
        computer = 'O'
    else:
        computer = 'X'
    return player, computer


def place_marker(board, marker, position):
    """Puts a player and computer marks to appropriate position"""
    if (position + 1) % 2:
        board[position] = f'| {marker} |'
        play_board_idx.remove(position)
    else:
        board[position] = marker
        play_board_idx.remove(position)


def check_place_marker(board, marker, position):
    """Test function arranges computer position for best choice position"""
    if (position + 1) % 2:
        board[position] = f'| {marker} |'
    else:
        board[position] = marker


def regex(string, mark):
    """Checks for the presence of a mark X or O in 5 in a row rule and return boolean value"""
    replaced = re.sub(r'[ |]', '', string)
    pattern = re.compile(r'([XO])\1{4}')
    match = re.findall(pattern, replaced)
    if mark in match:
        return True
    return False


def iterator(board, start, stop, step, offset):
    """Iteration by board uses start, stop, step and offset for getting all horizontal or all vertical rows"""
    rows = []
    for cell in range(n):
        rows.append(''.join([board[i] for i in range(start, stop, step)]))
        start -= offset
        stop -= offset
    return rows


def lose_check(board, mark):
    """Returns boolean value whether the player or the computer loses the game"""
    horizontal_rows = iterator(board, start=90, stop=100, step=1, offset=10)
    vertical_rows = iterator(board, start=9, stop=100, step=10, offset=1)
    diagonal_rows = [
        ''.join([board[i] for i in range(0, 100, 11)]),
        ''.join([board[i] for i in range(9, 91, 9)])
    ]
    rows = horizontal_rows + vertical_rows + diagonal_rows

    for row in rows:
        if regex(row, mark):
            return True
    return False


def space_check(board, position):
    """Returns boolean value whether the cell is free or not"""
    string = board[position]
    match = re.findall(r'[XO]', string)
    if len(match) == 0:
        return True


def full_board_check(board):
    """Returns boolean value whether the game board is full of game marks"""
    return len(set(board)) == 2


def player_choice(board, player_mark):
    """Gets player next position and check if it's appropriate to play"""
    position = None
    while position not in [num for num in range(0, 100)]:
        try:
            choice = input(f'Player "{player_mark}", choose your next position from 0 to 99 inclusive: ')
            if choice in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']:
                position = int(choice[1])
            else:
                position = int(choice)

        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')
        if isinstance(position, int) and position not in range(0, 100):
            print(f'Player "{player_mark}", please type a number from range 0 to 99 inclusive!')

    if space_check(board, position):
        return position
    else:
        """If the player chooses a non-free cell, then it is transferred to the player_choice function to fill exactly 
        the free cell"""
        print(f'Player "{player_mark}", please choose a free cell! The cell with the number {position} '
              f'is borrowed!')
        return player_choice(board, player_mark)


def replay():
    """Asks the player to play again"""
    decision = ''
    while decision not in ('y', 'n'):
        decision = input('Would you like to play again? (Type "y" or "n") ').lower()
    return decision == 'y'


def clear_screen():
    """Clears the game screen via adding new rows"""
    print('\n' * 100)


def switch_player(mark):
    """Switches between player and computer to play next turn"""
    return 'O' if mark == 'X' else 'X'


def check_game_finish(board, mark, player):
    """Return boolean value is the game finished or not"""
    if lose_check(board, mark):
        if mark == player:
            print(f'The player with the mark "{mark}" has lost out! Don\'t be upset, try it again!')
        else:
            print(f'The computer with the mark "{mark}" has lost out! Congratulations!')
        return True

    if full_board_check(play_board):
        print('The game ended in a draw')
        return True
    return False


def check_computer_can_loss_at_current_position(board, mark, position):
    """Check, if current computer position can call a loss"""
    board_copy = copy(board)
    check_place_marker(board_copy, mark, position)
    if lose_check(board_copy, mark):
        return True
    return False


print('Welcome to Reverse Tic Tac Toe!')
print('You\'ll play against the computer!')
print('The one who has a match of 5 figures horizontally, vertically or diagonally loses!')
player, computer = player_input()
current_mark = 'X'
if player == current_mark:
    print(f'Player with mark "{current_mark}" goes first according to the canon!')
else:
    print(f'The computer with mark "{current_mark}" goes first according to the canon!')

while True:
    if current_mark == player:
        display_board(play_board)
        print(f'Turn of the player with the mark "{current_mark}":')

        play_position = player_choice(play_board, current_mark)
        place_marker(play_board, current_mark, play_position)
    else:
        computer_position = random.choice(list(play_board_idx))
        play_board_idx_copy = copy(play_board_idx)

        while check_computer_can_loss_at_current_position(play_board, current_mark, computer_position):
            play_board_idx_copy.discard(computer_position)
            if len(play_board_idx_copy) == 0:
                break
            computer_position = random.choice(list(play_board_idx_copy))

        print(f'The computer with the mark "{current_mark} chose in his turn cell with the number": '
              f'{computer_position}')
        place_marker(play_board, current_mark, computer_position)

    if check_game_finish(play_board, current_mark, player):
        display_board(play_board)
        if not replay():
            break
        else:
            clear_screen()
            play_board = ['| - |' if num % 2 else '-' for num in range(1, 101)]
            play_board_idx = {idx for idx, i in enumerate(play_board)}
            print('Welcome to Reverse Tic Tac Toe!')
            print('You\'ll play against the computer!')
            print('The one who has a match of 5 figures horizontally, vertically or diagonally loses!')
            player, computer = player_input()
            current_mark = 'X'
            if player == current_mark:
                print(f'Player with mark "{current_mark}" goes first according to the canon')
            else:
                print(f'The computer with mark "{current_mark}" goes first according to the canon')
    else:
        current_mark = switch_player(current_mark)
