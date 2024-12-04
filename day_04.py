def main():
    WORD = "XMAS"
    MATRIX = []
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        MATRIX.append(line.rstrip())

    ROW = len(MATRIX)
    COL = len(MATRIX[0])

    def dfs(r, c, i, direction):
        if i == len(WORD):
            return True
        
        if r < 0 or r >= ROW or c < 0 or c >= COL or WORD[i] != MATRIX[r][c]:
            return False

        if direction == "left":
            res = dfs(r, c-1, i+1, direction) 
        elif direction == "right":
            res = dfs(r, c+1, i+1, direction)
        elif direction == "up":
            res = dfs(r-1, c, i+1, direction)
        elif direction == "down":
            res = dfs(r+1, c, i+1, direction)
        elif direction == "top_left":
            res = dfs(r-1, c-1, i+1, direction)
        elif direction == "top_right":
            res = dfs(r-1, c+1, i+1, direction)
        elif direction == "bottom_left":
            res = dfs(r+1, c-1, i+1, direction)
        elif direction == "bottom_right":
            res = dfs(r+1, c+1, i+1, direction)

        return res
    
    sum = 0
    for i in range(ROW):
        for j in range(COL):
            if MATRIX[i][j] == WORD[0]:
                if dfs(i, j, 0, "left"):
                    sum += 1
                if dfs(i, j, 0, "right"):
                    sum += 1
                if dfs(i, j, 0, "up"):
                    sum += 1
                if dfs(i, j, 0, "down"):
                    sum += 1
                if dfs(i, j, 0, "top_left"):
                    sum += 1
                if dfs(i, j, 0, "top_right"):
                    sum += 1
                if dfs(i, j, 0, "bottom_left"):
                    sum += 1
                if dfs(i, j, 0, "bottom_right"):
                    sum += 1
    print(sum)

    MATRIX = []
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    MATRIX.append("."+"."*len(lines[0]))
    for line in lines:
        MATRIX.append("."+line.rstrip()+".")
    MATRIX.append("."+"."*len(lines[0]))

    sum = 0
    ROW = len(MATRIX)
    COL = len(MATRIX[0])

    for i in range(1, ROW-1):
        for j in range(1, COL-1):
            if MATRIX[i][j] == "A":
                if MATRIX[i-1][j-1] == "M" and MATRIX[i+1][j-1] == "M" and MATRIX[i-1][j+1] == "S" and MATRIX[i+1][j+1] == "S":
                    sum += 1
                if MATRIX[i-1][j-1] == "S" and MATRIX[i+1][j-1] == "S" and MATRIX[i-1][j+1] == "M" and MATRIX[i+1][j+1] == "M":
                    sum += 1
                if MATRIX[i-1][j-1] == "M" and MATRIX[i+1][j-1] == "S" and MATRIX[i-1][j+1] == "M" and MATRIX[i+1][j+1] == "S":
                    sum += 1
                if MATRIX[i-1][j-1] == "S" and MATRIX[i+1][j-1] == "M" and MATRIX[i-1][j+1] == "S" and MATRIX[i+1][j+1] == "M":
                    sum += 1
    print(sum)

if __name__ == "__main__":
    main()
   