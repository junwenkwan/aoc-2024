def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    grid = [row.rstrip() for row in lines]
    
    num_row = len(grid)
    num_col = len(grid[0])

    look_up_map = {}
    for r in range(num_row):
        for c in range(num_col):
            val = grid[r][c]
            if val != ".":
                if val not in look_up_map:
                    look_up_map[val] = [(r,c)]
                else:
                    look_up_map[val].append((r,c))

    # part 1
    antinodes = set()
    for frequency in look_up_map:
        coords = look_up_map[frequency]
        for i in range(len(coords)-1):
            for j in range(i+1,len(coords)):
                val_1 = coords[i]
                val_2 = coords[j]
                diff = (val_2[0]-val_1[0], val_2[1]-val_1[1])
                
                antinode_1 =  (val_1[0]-diff[0],val_1[1]-diff[1])
                antinode_2 =  (val_2[0]+diff[0],val_2[1]+diff[1])
                
                if antinode_1[0] >= 0 and antinode_1[0] < num_row and antinode_1[1] >= 0 and antinode_1[1] < num_col:
                    antinodes.add(antinode_1)

                if antinode_2[0] >= 0 and antinode_2[0] < num_row and antinode_2[1] >= 0 and antinode_2[1] < num_col:
                    antinodes.add(antinode_2)

    print(len(antinodes))

    # part 2
    antinodes = set()
    for frequency in look_up_map:
        coords = look_up_map[frequency]
        for i in range(len(coords)-1):
            for j in range(i+1,len(coords)):
                val_1 = coords[i]
                val_2 = coords[j]
                diff = (val_2[0]-val_1[0], val_2[1]-val_1[1])
                antinodes.add(val_1)
                antinodes.add(val_2)
                while True:
                    antinode_1 = (val_1[0]-diff[0],val_1[1]-diff[1])
                    if (antinode_1[0] >= 0 and antinode_1[1] >= 0) and (antinode_1[0] < num_row and antinode_1[1] < num_col):
                        antinodes.add(antinode_1)
                    else:
                        break
                    
                    val_1 = antinode_1

                while True:
                    antinode_2 =  (val_2[0]+diff[0],val_2[1]+diff[1])

                    if antinode_2[0] >= 0 and antinode_2[0] < num_row and antinode_2[1] >= 0 and antinode_2[1] < num_col:
                        antinodes.add(antinode_2)
                    else:
                        break
                    
                    val_2 = antinode_2

    print(len(antinodes))

if __name__ == "__main__":
    main()