
def FindAntinodes(grid):
    m = len(grid)
    n = len(grid[0])
    AntinodeMap = [[False for i in range(n)] for k in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] != "." and grid[i][j] != "#":
                indices = FindExpandPair(grid,i,j,m,n)
                for index in indices:
                    try:
                        AntinodeMap[index[0]][index[1]] = True
                    except IndexError:
                        pass
    
    for i in range(m):
        for j in range(n):
            if AntinodeMap[i][j] == True:
                count += 1
    return count



def FindExpandPair(grid,row,col,maxrow,maxcol): #assumption: original is not "." or "#"
    antinodes = set()
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
            indices = ExtendLine(grid,row,col,maxrow,maxcol,dx,dy)
            for index in indices:
                antinodes.add(index)
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
            


def ExtendLine(grid,startrow,startcol,maxrow,maxcol,dx,dy):
    indices = []
    row = startrow+dx
    col = startcol+dy
    while ((row in range(0,maxrow)) and (col in range(maxcol))):
        indices.append((row,col))
        row += dx
        col += dy
    row = startrow
    col = startcol
    while ((row in range(0,maxrow)) and (col in range(maxcol))):
        indices.append((row,col))
        row = row - dx
        col = col - dy

    return indices
    

def TextToGrid(filenamestring):
    grid = []

    f = open(filenamestring,'r')
    for line in f:
        grid.append(list(line.rstrip()))

    f.close()

    return grid

grid = TextToGrid('input.txt')
print(FindAntinodes(grid))