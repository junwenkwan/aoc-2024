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

def traverse_up(grid, r, c):
    while r >= 0:
        if grid[r][c] == "#":
            break
        r -= 1
    return r, c

def traverse_down(grid, r, c):
    while r < len(grid):
        if grid[r][c] == "#":
            break
        r += 1
    return r, c

def traverse_left(grid, r, c):
    while c >= 0:
        if grid[r][c] == "#":
            break
        c -= 1
    return r, c

def traverse_right(grid, r, c):
    while c < len(grid[0]):
        if grid[r][c] == "#":
            break
        c += 1
    return r, c


def main():
    grid = ["....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#..."]
    
    grid = [list(row) for row in grid]

    guard_x, guard_y, guard_dir = find_guard_pos(grid)
    print(guard_x, guard_y, guard_dir)

if __name__ == "__main__":
    main()