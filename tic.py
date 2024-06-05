import random
def create_board():
    board = []
    for i in range(3):
        rows = []
        for j in range(3):
            rows.append("-")
        board.append(rows)
    return board

def display_board(board):
    for i in board:
        print(f'{i[0]} | {i[1]} | {i[2]}')
def welcome_message():
    print("==============================")
    print(f'Welcome to a Tic-Tac-Toe game!')
    print("==============================")

def invite_players_to_the_game():
    welcome_message()
    print(f'Enter your name as the first player')
    first_player = input()
    markers = ["X", "O"]
    random.shuffle(markers)
    first_player_marker = markers[0]
    second_player_marker = markers[1]
    print(f"Welcome on board {first_player}. Your marker is {first_player_marker}\n")
    print(f'Enter your name as the second player')
    second_player = input()
    print(f"Welcome on board {second_player}. Your marker is {second_player_marker}\n")
    player_info_list = [{"name": first_player, "marker": first_player_marker},
            {"name": second_player, "marker": second_player_marker}]
    random.shuffle(player_info_list)
    return player_info_list

def play():
    players = invite_players_to_the_game()
    print(f'This is how the board looks like initially:')
    board = create_board()
    display_board(board)
    print(f'To play, enter position (1-9) from left to right and from top to bottom:\n')
    play_in_turns(board, players)

def get_indices(position):
    row = (position - 1) // 3
    col = (position - 1) % 3
    return (row, col)

def check_if_position_is_occupied(board, position):
    indices = get_indices(position)
    row = indices[0]
    col = indices[1]
    return board[row][col] != "-"

def check_if_board_is_full(board):
    return '-' not in flatten_board(board)

def flatten_board(board):
    flattened = []
    for i in board:
        for j in i:
            flattened.append(j)
    return flattened

def check_win(board):
    if len(set(board[0])) == 1 and "-" not in board[0]:
        return True
    if len(set(board[1])) == 1 and "-" not in board[1]:
        return True
    if len(set(board[1])) == 1 and "-" not in board[1]:
        return True
    column1 = [board[0][0], board[1][0], board[2][0]]
    if len(set(column1)) == 1 and "-" not in column1:
        return True
    column2 = [board[0][1], board[1][1], board[2][1]]
    if len(set(column2)) == 1 and "-" not in column2:
        return True
    column3 = [board[0][2], board[1][2], board[2][2]]
    if len(set(column3)) == 1 and "-" not in column3:
        return True
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    if len(set(diagonal1)) == 1 and "-" not in diagonal1:
        return True
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    if len(set(diagonal2)) == 1 and "-" not in diagonal2:
        return True
    else:
        return False
    
def make_user_input(name, print_prompt=True):
    if print_prompt:
        print(f"{name}, Make your move now")
    position = input()
    is_digit = True
    while is_digit:
        try:
            position = int(position)
            is_digit = False
        except:
            print(f"{name}, you have entered a non-digit. Try again!")
            position = input()
    return position

def check_range_validity(name, position):
    valid = 0 < position < 10
    while not valid:
        print(f"{name}, your entry is not in the range (1-9). Try again!")
        position = make_user_input(name, print_prompt=False)
        valid = 0 < position < 10
    return position

def update_occupied_positions(board, position, name, marker):
    occupied = check_if_position_is_occupied(board, position)
    while occupied:
        print(f'Hey {name}, That position seems to be occupied! Try again')
        position = make_user_input(name, print_prompt=False)
        display_board(board)
        occupied = check_if_position_is_occupied(board, position)
    else:
        indices = get_indices(position)
        row = indices[0]
        col = indices[1]
        board[row][col] = marker
    return board

def play_in_turns(board, players):
    inplay = True
    while inplay:
        for player in players:
            name = player["name"]
            marker = player["marker"]
            position = check_range_validity(name=name, position=make_user_input(name))
            board = update_occupied_positions(board, position, name, marker)
            display_board(board)

            if check_win(board):
                print(f'{name} wins!')
                inplay = False
                break

            if check_if_board_is_full(board):
                print("It's a draw")
                inplay = False
                break

if __name__ == "__main__":
    play()
    # board = [["-", "-", "-"], [2, 3, 2], [2, 4, 8]]
    # print(check_range_validity("Joseph", 10))
  