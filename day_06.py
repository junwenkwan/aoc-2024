from tqdm import tqdm

def find_guard_pos(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                return r, c, "^"
            if grid[r][c] == "<":
                return r, c, "<"
            if grid[r][c] == ">":
                return r, c, ">"
            if grid[r][c] == "v":
                return r, c, "v"

def start(x, y, dir, grid, NUM_ROW, NUM_COL):
    tiles = set()
    is_loop = False
    tiles_dir = set()

    while True:
        tiles.add((x,y))
        tiles_dir.add((x,y,dir))

        if dir == "^":
            x -= 1
        elif dir == ">":
            y += 1
        elif dir == "v":
            x += 1
        elif dir == "<":
            y -= 1

        if x < 0 or y < 0 or x >= NUM_ROW or y >= NUM_COL:
            break

        if (x,y,dir) in tiles_dir:
            is_loop = True
            break
        
        if grid[x][y] == "#":
            if dir == "^":
                x += 1
                dir = ">"
            elif dir == ">":
                y -= 1
                dir = "v"
            elif dir == "v":
                x -= 1
                dir = "<"
            elif dir == "<":
                y += 1
                dir = "^"

    return tiles, is_loop

def main():
    # part 1
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    grid = [list(row.rstrip()) for row in lines]
    
    grid = [list(row) for row in grid]
    
    NUM_ROW = len(grid)
    NUM_COL = len(grid[0])

    x_init, y_init, dir_init = find_guard_pos(grid)
    print("Starting position:", x_init, y_init, dir_init)

    tiles, _ = start(x_init, y_init, dir_init, grid, NUM_ROW, NUM_COL)
    
    print(len(tiles))

    # part 2
    place_obstacles = tiles.copy()
    sum_loop = 0
    replace = False

    for item in tqdm(place_obstacles):
        r_o = item[0]
        c_o = item[1]
        if grid[r_o][c_o] == ".":
            grid[r_o][c_o] = "#"
            replace = True
        else:
            continue

        _, is_loop = start(x_init, y_init, dir_init, grid, NUM_ROW, NUM_COL)
        
        if replace:
            grid[r_o][c_o] = "."
            replace = False

        if is_loop:
            sum_loop += 1

    print(sum_loop)

if __name__ == "__main__":
    main()