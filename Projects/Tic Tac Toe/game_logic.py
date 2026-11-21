"""Contains all the functions to make the game work."""

def get_score() -> None:
    return None

def player_turn(player: int) -> int:
    if player == 1:
        player = 2
    else:
        player = 1
    return player

def playing_field() -> list[list]:
    playing_field = [
      [" ", " ", " "]
      [" ", " ", " "]
      [" ", " ", " "]
    ]

def player_input() -> None:
    input_initial = input()

def player_move(initial_input: int) -> tuple:
    move_index = (row, column)
    match initial_input:
        case 1:
            move_index = (0, 0)
        case 2:
            move_index = (0, 1)
        case 3:
            move_index = (0, 2)
        case 4:
            move_index = (1, 0)
        case 5:
            move_index = (1, 1)
        case 6:
            move_index = (1, 2)
        case 7:
            move_index = (2, 0)
        case 8:
            move_index = (2, 1)
        case 9:
            move_index = (2, 2)
    return move_index              

def player_tick(player: int) -> str:
    match player:
        case 1:
            player_tick = "X"
        case 2:
            playrr_tick = "O"
    return player_tick

def victory_status(win_stat_field: list[list) -> bool:
    cell_value_to_win = 3
    for row in win_stat_field:
        if cell_value_to_win in row:
            return True
    return False

def winner(victory_status: bool, player: int) -> int:
    no_one_won = 0
    if not victory_status:
        return no_one_won
    else: 
        return player
        
