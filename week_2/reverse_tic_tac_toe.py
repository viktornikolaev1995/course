"""Reverse Tic-Tac-Toe game"""
from copy import copy
import random
import re


play_board = [str(num) for num in range(1, 101)]
play_board_idx = {idx for idx, i in enumerate(play_board)}
players_marks = ['X', 'O']


def display_board(board_list):
    """Prints the game board"""
    print(board_list[99] + ' | ' + board_list[98] + ' | ' + board_list[97] + ' | ' + board_list[96] + ' | '
          + board_list[95] + ' | ' + board_list[94] + ' | ' + board_list[93] + ' | ' + board_list[92] + ' | ' +
          board_list[91] + ' | ' + board_list[90] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[89] + ' | ' + board_list[88] + ' | ' + board_list[87] + ' | ' + board_list[86] + ' | '
          + board_list[85] + ' | ' + board_list[84] + ' | ' + board_list[83] + ' | ' + board_list[82] + ' | ' +
          board_list[81] + ' | ' + board_list[80] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[79] + ' | ' + board_list[78] + ' | ' + board_list[77] + ' | ' + board_list[76] + ' | '
          + board_list[75] + ' | ' + board_list[74] + ' | ' + board_list[73] + ' | ' + board_list[72] + ' | ' +
          board_list[71] + ' | ' + board_list[70] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[69] + ' | ' + board_list[68] + ' | ' + board_list[67] + ' | ' + board_list[66] + ' | '
          + board_list[65] + ' | ' + board_list[64] + ' | ' + board_list[63] + ' | ' + board_list[62] + ' | ' +
          board_list[61] + ' | ' + board_list[60] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[59] + ' | ' + board_list[58] + ' | ' + board_list[57] + ' | ' + board_list[56] + ' | '
          + board_list[55] + ' | ' + board_list[54] + ' | ' + board_list[53] + ' | ' + board_list[52] + ' | ' +
          board_list[51] + ' | ' + board_list[50] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[49] + ' | ' + board_list[48] + ' | ' + board_list[47] + ' | ' + board_list[46] + ' | '
          + board_list[45] + ' | ' + board_list[44] + ' | ' + board_list[43] + ' | ' + board_list[42] + ' | ' +
          board_list[41] + ' | ' + board_list[40] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[39] + ' | ' + board_list[38] + ' | ' + board_list[37] + ' | ' + board_list[36] + ' | '
          + board_list[35] + ' | ' + board_list[34] + ' | ' + board_list[33] + ' | ' + board_list[32] + ' | ' +
          board_list[31] + ' | ' + board_list[30] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[29] + ' | ' + board_list[28] + ' | ' + board_list[27] + ' | ' + board_list[26] + ' | '
          + board_list[25] + ' | ' + board_list[24] + ' | ' + board_list[23] + ' | ' + board_list[22] + ' | ' +
          board_list[21] + ' | ' + board_list[20] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[19] + ' | ' + board_list[18] + ' | ' + board_list[17] + ' | ' + board_list[16] + ' | '
          + board_list[15] + ' | ' + board_list[14] + ' | ' + board_list[13] + ' | ' + board_list[12] + ' | ' +
          board_list[11] + ' | ' + board_list[10] + ' ')
    print(' -- | -- | -- | -- | -- | -- | -- | -- | -- | -- ')
    print(' ' + board_list[9] + ' |  ' + board_list[8] + ' |  ' + board_list[7] + ' |  ' + board_list[6] + ' |  '
          + board_list[5] + ' |  ' + board_list[4] + ' |  ' + board_list[3] + ' |  ' + board_list[2] + ' |  ' +
          board_list[1] + ' |  ' + board_list[0] + ' ')


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
    if len(board[position]) == 3:
        board[position] = f'  {marker}'
        play_board_idx.remove(position)
    elif len(board[position]) == 2:
        board[position] = f' {marker}'
        play_board_idx.remove(position)
    else:
        board[position] = marker
        play_board_idx.remove(position)


def check_place_marker(board, marker, position) :
    """Test function arranges computer position for best choice position"""
    if len(board[position]) == 3:
        board[position] = f'  {marker}'
    elif len(board[position]) == 2:
        board[position] = f' {marker}'
    else:
        board[position] = marker


def regex(string, mark):
    """This regular expression checks for the presence of a mark X or O in 5 in a row rule"""
    string = string.replace(" ", "")
    pattern = re.compile(r'([XO])\1{4}')
    match = re.findall(pattern, string)
    if mark in match:
        return True
    return False


def lose_check(board, mark):
    """Returns boolean value whether the player or the computer loses the game"""
    rows = [
        f'{board[99]}{board[98]}{board[97]}{board[96]}{board[95]}{board[94]}{board[93]}{board[92]}{board[91]}'
        f'{board[90]}',   # 1 horizontal
        f'{board[89]}{board[88]}{board[87]}{board[86]}{board[85]}{board[84]}{board[83]}{board[82]}{board[81]}'
        f'{board[80]}'    # 2 horizontal
        f'{board[79]}{board[78]}{board[77]}{board[76]}{board[75]}{board[74]}{board[73]}{board[72]}{board[71]}'
        f'{board[70]}',   # 3 horizontal
        f'{board[69]}{board[68]}{board[67]}{board[66]}{board[65]}{board[64]}{board[63]}{board[62]}{board[61]}'
        f'{board[60]}',   # 4 horizontal
        f'{board[59]}{board[58]}{board[57]}{board[56]}{board[55]}{board[54]}{board[53]}{board[52]}{board[51]}'
        f'{board[50]}',   # 5 horizontal
        f'{board[49]}{board[48]}{board[47]}{board[46]}{board[45]}{board[44]}{board[43]}{board[42]}{board[41]}'
        f'{board[40]}',   # 6 horizontal
        f'{board[39]}{board[38]}{board[37]}{board[36]}{board[35]}{board[34]}{board[33]}{board[32]}{board[31]}'
        f'{board[30]}',   # 7 horizontal
        f'{board[29]}{board[28]}{board[27]}{board[26]}{board[25]}{board[24]}{board[23]}{board[22]}{board[21]}'
        f'{board[20]}',   # 8 horizontal
        f'{board[19]}{board[18]}{board[17]}{board[16]}{board[15]}{board[14]}{board[13]}{board[12]}{board[11]}'
        f'{board[10]}',   # 9 horizontal
        f'{board[9]}{board[8]}{board[7]}{board[6]}{board[5]}{board[4]}{board[3]}{board[2]}{board[1]}'
        f'{board[0]}',    # 10 horizontal
        f'{board[99]}{board[89]}{board[79]}{board[69]}{board[59]}{board[49]}{board[39]}{board[29]}{board[19]}'
        f'{board[9]}',    # 1 vertical
        f'{board[98]}{board[88]}{board[78]}{board[68]}{board[58]}{board[48]}{board[38]}{board[28]}{board[18]}'
        f'{board[8]}',    # 2 vertical
        f'{board[97]}{board[87]}{board[77]}{board[67]}{board[57]}{board[47]}{board[37]}{board[27]}{board[17]}'
        f'{board[7]}',    # 3 vertical
        f'{board[96]}{board[86]}{board[76]}{board[66]}{board[56]}{board[46]}{board[36]}{board[26]}{board[16]}'
        f'{board[6]}',    # 4 vertical
        f'{board[95]}{board[85]}{board[75]}{board[65]}{board[55]}{board[45]}{board[35]}{board[25]}{board[15]}'
        f'{board[5]}',    # 5 vertical
        f'{board[94]}{board[84]}{board[74]}{board[64]}{board[54]}{board[44]}{board[34]}{board[24]}{board[14]}'
        f'{board[4]}',    # 6 vertical
        f'{board[93]}{board[83]}{board[73]}{board[63]}{board[53]}{board[43]}{board[33]}{board[23]}{board[13]}'
        f'{board[3]}',    # 7 vertical
        f'{board[92]}{board[82]}{board[72]}{board[62]}{board[52]}{board[42]}{board[32]}{board[22]}{board[12]}'
        f'{board[2]}',    # 8 vertical
        f'{board[91]}{board[81]}{board[71]}{board[61]}{board[51]}{board[41]}{board[31]}{board[21]}{board[11]}'
        f'{board[1]}',    # 9 vertical
        f'{board[90]}{board[80]}{board[70]}{board[60]}{board[50]}{board[40]}{board[30]}{board[20]}{board[10]}'
        f'{board[0]}',    # 10 vertical
        f'{board[99]}{board[88]}{board[77]}{board[66]}{board[55]}{board[44]}{board[33]}{board[22]}{board[11]}'
        f'{board[0]}',    # 1 diagonal
        f'{board[9]}{board[18]}{board[27]}{board[36]}{board[45]}{board[54]}{board[63]}{board[72]}{board[81]}'
        f'{board[90]}'    # 2 diagonal
    ]

    for row in rows:
        if regex(row, mark):
            return True
    return False


def space_check(board, position):
    """Returns boolean value whether the cell is free or not"""
    mark = board[position].replace(" ", "")
    if mark not in players_marks:
        return True


def full_board_check(board):
    """Returns boolean value whether the game board is full of game marks"""
    return len(set(board)) == 2


def player_choice(board, player_mark):
    """Gets player next position and check if it's appropriate to play"""
    position = 0
    while position not in [num for num in range(1, 101)]:
        try:
            position = \
                int(input(f'Player "{player_mark}", choose your next position from 1 to 100: '))
        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')

    position -= 1
    if space_check(board, position):
        return position
    else:
        """If the player chooses a non-free cell, then it is transferred to the player_choice function
            to fill exactly the free cell"""
        print(f'Player "{player_mark}", please choose a free cell! The cell with the number {position + 1} '
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
            print(f'In this position computer can be loss: {computer_position}')
            print(f'play_board_idx_copy: {play_board_idx_copy}')
            play_board_idx_copy.discard(computer_position)
            if len(play_board_idx_copy) == 0:
                break
            computer_position = random.choice(list(play_board_idx_copy))
            print(f'Selecting the following position: {computer_position}')

        print(f'The computer with the mark "{current_mark} chose in his turn cell with the number": '
              f'{computer_position + 1}')
        place_marker(play_board, current_mark, computer_position)

    if check_game_finish(play_board, current_mark, player):
        display_board(play_board)
        if not replay():
            break
        else:
            clear_screen()
            play_board = [str(num) for num in range(1, 101)]
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
