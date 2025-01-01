def FindAntinodes(grid):
    m = len(grid)
    n = len(grid[0])
    AntinodeMap = [[False for i in range(n)] for k in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] != "." and grid[i][j] != "#":
                indices = FindPair(grid,i,j,m,n)
                for index in indices:
                    AntinodeMap[index[0]][index[1]] = True
    
    for i in range(m):
        for j in range(n):
            if AntinodeMap[i][j] == True:
                count += 1
    return count



def FindPair(grid,row,col,maxrow,maxcol): #assumption: original is not "." or "#"
    antinodes = []
    original = grid[row][col]
    originalrow = row
    originalcol = col
    while row!=maxrow-1 or col!=maxcol-1:
        if originalcol == col and originalrow == row:
            if col<maxcol-1:
                col+=1
            else:
                col = 0
                row += 1
        elif grid[row][col] == original:
            dx = row- originalrow
            dy = col- originalcol
            tailhead_row_index = [originalrow-dx,row+dx]
            tailhead_col_index = [originalcol-dy,col+dy]
            tailinside = [tailhead_row_index[0] in range(0,maxrow),tailhead_col_index[0] in range(0,maxcol)]
            headinside = [tailhead_row_index[1] in range(0,maxrow), tailhead_col_index[1] in range(0,maxcol)]
            combined = tailinside+headinside

            if all(combined):
                antinodes.append([originalrow-dx,originalcol-dy])
                antinodes.append([row+dx,col+dy])
                if col<maxcol-1:
                    col+=1
                else:
                    col = 0
                    row += 1
            elif all(tailinside):
                antinodes.append([originalrow-dx,originalcol-dy])
                if col<maxcol-1:
                    col+=1
                else:
                    col = 0
                    row += 1
            elif all(headinside):
                antinodes.append([row+dx,col+dy])
                if col<maxcol-1:
                    col+=1
                else:
                    col = 0
                    row += 1
            else:
                if col<maxcol-1:
                    col+=1
                else:
                    col = 0
                    row += 1
        else:
            if col<maxcol-1:
                col+=1
            else:
                col = 0
                row += 1
    return antinodes
            



def TextToGrid(filenamestring):
    grid = []

    f = open(filenamestring,'r')
    for line in f:
        grid.append(list(line.rstrip()))

    f.close()

    return grid

grid = TextToGrid('input.txt')
print(FindAntinodes(grid))