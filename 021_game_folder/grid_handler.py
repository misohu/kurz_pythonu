def create_grid(rows, cols, empty_sign="_"):
    grid=[]
    for row in range(0, rows):
        temp_row = []
        for col in range(0, cols):
            temp_row.append("_")
        grid.append(temp_row)
    return grid

def print_grid(grid, rows, cols):
    print(" ", end=" ")
    for col in range(0, cols):
        print(col, end=" ")
    print()
    for row in range(0, rows):
        print(row, end=" ")
        for col in range(0, cols):
            print(grid[row][col], end=" ")
        print()