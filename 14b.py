def GuardPositions(maxrow,maxcol,guard_info,seconds):

    guards_id = guard_info.keys()
    t=0

    while True:
        for id in guards_id:
            x, y = GuardEndPosition(guard_info[id][0],guard_info[id][1],1,maxrow,maxcol)
            guard_info[id][0] = (x,y)
        positions = [guard_info[id][0] for id in guards_id]
        t+=1
        if len(set(positions)) == 500:
            DisplayGuards(maxrow,maxcol,positions)
            print(t)
            break

def GuardEndPosition(start_pos,movement_vector,seconds,maxrow,maxcol):
    x_start, y_start = start_pos[0], start_pos[1]

    dx, dy = movement_vector[0], movement_vector[1]

    x_end = (x_start + dx * seconds) % maxrow
    y_end = (y_start + dy * seconds) % maxcol

    return x_end,y_end


def TextToGuards(filenamestring):
    """
    Input: 14a AdventOfCode
    Output: Dictionary with keys from 1,...,n, where n is the number of guards. Each key is assigned to a guard starting pos with corresponding guard vector
    """
    f = open(filenamestring,'r')
    index = 0
    guards = dict() # no. of guard : [start_pos,movement_vector]

    for line in f:
        stripped_line = line.rstrip()
        stripped_line = stripped_line.split(sep = " ")
        startpos = [int(stripped_line[0][2:].split(sep = ",")[1]),int(stripped_line[0][2:].split(sep = ",")[0])]
        movement_vector = [int(stripped_line[1][2:].split(sep=",")[1]),int(stripped_line[1][2:].split(sep=",")[0])]
        guards[index] = [startpos,movement_vector]
        index += 1

    return guards
def DisplayGuards(maxrow,maxcol,guardpositions):
    grid = [[" " for j in range(maxcol)] for i in range(maxrow)]

    for guard_position in guardpositions:
        x,y =guard_position[0], guard_position[1]

        grid[x][y] = "*"
    for i in range(len(grid)):
        grid[i] = "".join(grid[i])
    print(*grid,sep="\n")
    
guard_info = TextToGuards('input.txt')
GuardPositions(103,101,guard_info,200)
