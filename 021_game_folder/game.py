from grid_handler import print_grid, create_grid
from input_handler import get_input
from game_handler import check_game

rows = 3
cols = 3
empty_sign="_"
player_symbols={
    1: "x",
    2: "o"
}
winner=False

grid = create_grid(rows, cols, empty_sign)
empty_places = rows*cols

for round_id in range(0, round(rows*cols/2) + 1):
    print(f"Round n.o. {round_id}") 
    for player_id in range(1, 3):
        while True:
            print_grid(grid, rows, cols)
            print(f"Player{player_id}, x coordinate:")
            x = get_input()
            print(f"Player{player_id}, y coordinate:")
            y = get_input()

            if x >= rows or x < 0 or y >= cols or y < 0:
                print("Position out of game field, please insert correct position")
                continue

            if grid[x][y] == empty_sign:
                break
            else:
                print("Sorry this position is already taken")

        grid[x][y] = player_symbols[player_id]
        if check_game(grid, player_symbols[player_id], rows, cols):
            print(f"Player {player_id} wins !!!!!")
            winner=True
            break
        empty_places -=1
        0
        if empty_places == 0:
            break 
    
    if winner:
        print_grid(grid, rows, cols)
        break

    if empty_places == 0:
        print_grid(grid, rows, cols)
        print("Game ended with draw")
        break 



    