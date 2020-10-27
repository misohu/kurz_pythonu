def check_game(grid, player_symbol, rows, columns):
    # check rows
    for i in range(0, rows):
        if grid[i][:] == [player_symbol] * columns:
            return True
    
    # check columns
    for i in range(0, columns):
        temp_column = []
        for row in range(0, rows):
            temp_column.append(grid[row][i])
        if temp_column == [player_symbol] * rows:
            return True
    
    # First diagonal
    temp_column = []
    for i in range(0, rows):
        temp_column.append(grid[i][i])
    if temp_column == [player_symbol] * rows:
        return True
    
    # Second diagonal
    temp_column = []
    for i in range(0, rows):
        temp_column.append(grid[i][rows - i - 1])
    if temp_column == [player_symbol] * rows:
        return True

    return False