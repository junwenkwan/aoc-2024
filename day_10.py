from collections import deque

def main():
    def bfs(r, c):
        score = 0
        DEQUE = deque([(r,c)])
        VISITED_NODES = set()
        
        while DEQUE:
            r_current, c_current = DEQUE.popleft()

            if (r_current, c_current) in VISITED_NODES:
                continue
            
            VISITED_NODES.add((r_current, c_current))
            
            if GRID[r_current][c_current] == "9":
                score += 1
            
            for direction in DIRECTIONS:
                dr, dc = direction
                r_next = r_current + dr
                c_next = c_current + dc
                
                if 0 <= r_next < NUM_ROW and 0 <= c_next < NUM_COL and int(GRID[r_next][c_next]) == int(GRID[r_current][c_current]) + 1:
                    DEQUE.append((r_next, c_next))
                    
        return score

    def dfs(r_current, c_current):
        if GRID[r_current][c_current] == "9":
            return 1
        
        rating = 0        
        
        for direction in DIRECTIONS:
            dr, dc = direction
            r_next = r_current + dr
            c_next = c_current + dc
            
            if 0 <= r_next < NUM_ROW and 0 <= c_next < NUM_COL and int(GRID[r_next][c_next]) == int(GRID[r_current][c_current]) + 1:
                rating += dfs(r_next, c_next)
                
        return rating
    
    with open("./input.txt", "r") as f:
        lines = f.readlines()
            
    GRID = [row.rstrip() for row in lines]

    NUM_ROW = len(GRID)
    NUM_COL = len(GRID[0])

    DIRECTIONS = [(-1,0), (0,1), (1,0), (0,-1)] # up, left, down, right

    p1_ans = 0
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if GRID[r][c] == "0":
                score = bfs(r, c)
                p1_ans += score

    print(p1_ans)

    p2_ans = 0
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if GRID[r][c] == "0":
                rating = dfs(r, c)
                p2_ans += rating
                
    print(p2_ans)

if __name__ == "__main__":
    main()