def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
            
    GARDEN = [row.rstrip() for row in lines]

    directions = [(-1,0), (0,1), (1,0), (0,-1)]

    num_row = len(GARDEN)
    num_col = len(GARDEN[0])

    # part 1
    visited_nodes = set()
    p1_ans = 0
    for i in range(num_row):
        for j in range(num_col):
            if (i,j) in visited_nodes:
                continue

            queue = [(i,j)]
            area = 0
            perimeter = 0

            while queue:
                r_current, c_current = queue.pop()
                if (r_current, c_current) in visited_nodes:
                    continue
                visited_nodes.add((r_current, c_current))
                area += 1

                for dir in directions:
                    r_next = r_current + dir[0]
                    c_next = c_current + dir[1]

                    if 0 <= r_next < num_row and 0 <= c_next < num_col and GARDEN[r_current][c_current] == GARDEN[r_next][c_next]:
                        queue.append((r_next, c_next))
                    else:
                        perimeter += 1

            p1_ans += area * perimeter
    
    print(p1_ans)

    # part 2
    delimitor = "."
    for i, line in enumerate(GARDEN):
        line = delimitor + line + delimitor
        GARDEN[i] = line
        num_col = len(line)

    GARDEN.insert(0, delimitor*num_col)
    GARDEN.insert(num_row+1, delimitor*num_col)

    num_row = len(GARDEN)
    num_col = len(GARDEN[0])

    visited_nodes = set()
    p2_ans = 0
    for i in range(num_row):
        for j in range(num_col):
            if GARDEN[i][j] == delimitor:
                continue
            
            if (i,j) in visited_nodes:
                continue

            queue = [(i,j)]
            area = 0
            corners = 0

            while queue:
                r_current, c_current = queue.pop()
                if (r_current, c_current) in visited_nodes:
                    continue

                visited_nodes.add((r_current, c_current))
                area += 1

                # positive corners
                if GARDEN[r_current][c_current] != GARDEN[r_current-1][c_current] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current][c_current+1]:
                    corners += 1
                    
                if GARDEN[r_current][c_current] != GARDEN[r_current][c_current+1] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current+1][c_current]:
                    corners += 1

                if GARDEN[r_current][c_current] != GARDEN[r_current+1][c_current] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current][c_current-1]:
                    corners += 1
                    
                if GARDEN[r_current][c_current] != GARDEN[r_current][c_current-1] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current-1][c_current]:
                    corners += 1
                
                # negative corners
                if GARDEN[r_current][c_current] == GARDEN[r_current-1][c_current] and \
                   GARDEN[r_current][c_current] == GARDEN[r_current][c_current+1] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current-1][c_current+1]:
                    corners += 1
                
                if GARDEN[r_current][c_current] == GARDEN[r_current][c_current+1] and \
                   GARDEN[r_current][c_current] == GARDEN[r_current+1][c_current] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current+1][c_current+1]:
                    corners += 1

                if GARDEN[r_current][c_current] == GARDEN[r_current+1][c_current] and \
                   GARDEN[r_current][c_current] == GARDEN[r_current][c_current-1] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current+1][c_current-1]:
                    corners += 1

                if GARDEN[r_current][c_current] == GARDEN[r_current][c_current-1] and \
                   GARDEN[r_current][c_current] == GARDEN[r_current-1][c_current] and \
                   GARDEN[r_current][c_current] != GARDEN[r_current-1][c_current-1]:
                    corners += 1

                for dir in directions:
                    r_next = r_current + dir[0]
                    c_next = c_current + dir[1]

                    if 0 <= r_next < num_row and 0 <= c_next < num_col and GARDEN[r_current][c_current] == GARDEN[r_next][c_next]:
                        queue.append((r_next, c_next))
                    
            p2_ans += area * corners

    print(p2_ans)

if __name__ == "__main__":
    main()