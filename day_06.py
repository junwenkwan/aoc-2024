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
    return -1, -1, "X"

def traverse_up(grid, r, c, possible_pos):
    while r >= 0:
        if grid[r][c] == "#":
            break
        possible_pos.add((r,c))
        r -= 1
    return r, c, possible_pos

def traverse_down(grid, r, c, possible_pos):
    while r < len(grid):
        if grid[r][c] == "#":
            break
        possible_pos.add((r,c))
        r += 1
    return r, c, possible_pos

def traverse_left(grid, r, c, possible_pos):
    while c >= 0:
        if grid[r][c] == "#":
            break
        possible_pos.add((r,c))
        c -= 1
    return r, c, possible_pos

def traverse_right(grid, r, c, possible_pos):
    while c < len(grid[0]):
        if grid[r][c] == "#":
            break
        possible_pos.add((r,c))
        c += 1
    return r, c, possible_pos

def start(x, y, dir, grid, NUM_ROW, NUM_COL, obstacles, guard_possible_pos):
    is_loop = False
    
    while True:
        if x < 0 or y < 0 or x >= NUM_ROW-1 or y >= NUM_COL-1:
            break

        if dir == "^":
            o_x, o_y, guard_possible_pos = traverse_up(grid, x, y, guard_possible_pos)
            dir = ">" # turn right 90 deg
            obstacles.add((o_x, o_y))
            x = o_x + 1
        elif dir == ">":
            o_x, o_y, guard_possible_pos = traverse_right(grid, x, y, guard_possible_pos)
            dir = "v" # turn right 90 deg
            obstacles.add((o_x, o_y))
            y = o_y - 1
        elif dir == "v":
            o_x, o_y, guard_possible_pos = traverse_down(grid, x, y, guard_possible_pos)
            dir = "<" # turn right 90 deg
            obstacles.add((o_x, o_y))
            x = o_x - 1
        elif dir == "<":
            o_x, o_y, guard_possible_pos = traverse_left(grid, x, y, guard_possible_pos)
            dir = "^" # turn right 90 deg
            obstacles.add((o_x, o_y))
            y = o_y + 1

    return is_loop, guard_possible_pos

def main():
    # part 1
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    grid = [list(row.rstrip()) for row in lines]

    # grid = ["....#.....",
    #         ".........#",
    #         "..........",
    #         "..#.......",
    #         ".......#..",
    #         "..........",
    #         ".#..^.....",
    #         "........#.",
    #         "#.........",
    #         "......#..."]
    
    grid = [list(row) for row in grid]

    NUM_ROW = len(grid)
    NUM_COL = len(grid[0])

    x_init, y_init, dir_init = find_guard_pos(grid)
    print("Starting position:", x_init, y_init, dir_init)

    guard_possible_pos = set()
    obstacles = set()
    _, guard_possible_pos = start(x_init, y_init, dir_init, grid, NUM_ROW, NUM_COL, obstacles, guard_possible_pos)
    print(len(guard_possible_pos))

    # part 2
    # place_obstacles = guard_possible_pos.copy()
    # sum_loop = 0
    # obstacles = set()
    # replace = False
    # for r_o, c_o in tqdm(place_obstacles):
    #     if r_o == 73 and c_o ==41:
    #         continue

    #     if grid[r_o][c_o] == ".":
    #         grid[r_o][c_o] = "#"
    #         replace = True
    #     else:
    #         continue
    #     is_loop = start(x, y, dir, grid, NUM_ROW, NUM_COL, set(), set())
    #     if replace:
    #         grid[r_o][c_o] = "."
    #         replace = False
    #     if is_loop:
    #         sum_loop += 1

    # for r_o in tqdm.tqdm(range(NUM_ROW)):
    #     for c_o in range(NUM_COL):
    #         if grid[r_o][c_o] == ".":
    #             grid[r_o][c_o] = "#"
    #             replace = True
    #         else:
    #             continue
    #         obstacles = set()
    #         is_loop = start(x, y, dir, grid, NUM_ROW, NUM_COL, obstacles, guard_possible_pos)
    #         if replace:
    #             grid[r_o][c_o] = "."
    #             replace = False
    #         if is_loop:
    #             sum_loop += 1
    #             print(f"Placing obs at {r_o},{c_o} will create a loop, total loop found {sum_loop}")
    
    # print(sum_loop)
    # 1920 too high

if __name__ == "__main__":
    main()