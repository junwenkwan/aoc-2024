import heapq
from tqdm import tqdm

def path_finding(grid, byte_pos, num_bytes, num_row, num_col):
    for i in range(num_bytes):
        coords = byte_pos[i]
        x,y = coords.split(",")
        grid[int(y)][int(x)] = "#"

    start_r, start_c = 0, 0

    queue = []
    heapq.heappush(queue, (0, start_r, start_c, 0, 1))

    visited_nodes = set((start_r, start_c, 0, 1))

    while queue:
        cost, r, c, dr, dc = heapq.heappop(queue)
        visited_nodes.add((r, c, dr, dc))

        if r == num_row-1 and c == num_col-1:
            return cost
        
        for next_cost, next_r, next_c, next_dr, next_dc in [(cost+1,r+dr,c+dc,dr,dc), (cost,r,c,dc,-dr), (cost,r,c,-dc,dr)]:
            if next_r >= num_row or next_c >= num_col:
                continue

            if grid[next_r][next_c] == "#":
                continue

            if (next_r, next_c, next_dr, next_dc) in visited_nodes:
                continue
            
            if 0 <= next_r < num_row and 0 <= next_c < num_col:
                heapq.heappush(queue, (next_cost, next_r, next_c, next_dr, next_dc))

def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    byte_pos = []

    for line in lines:
        byte_pos.append(line.rstrip())

    num_row, num_col = 71, 71
    
    grid = []

    for r in range(num_row):
        grid.append(["." for c in range(num_col)])

    cost = path_finding(grid, byte_pos, 1024, num_row, num_col)
    print(cost)

    for i in tqdm(range(len(byte_pos))):
        cost = path_finding(grid, byte_pos, i+1, num_row, num_col)
        if cost is None:
            print(byte_pos[i])
            break

if __name__ == "__main__":
    main()