def SafetyFactor(maxrow,maxcol,guard_info,seconds):
    x_middle = maxrow//2
    y_middle = maxcol//2
    quadrant_population = [0 for _ in range(4)]
    guards_id = guard_info.keys()

    sfactor  = 0

    for id in guards_id:
        start_pos, movement_vector = guard_info[id][0], guard_info[id][1]
        x,y = GuardEndPosition(start_pos,movement_vector,seconds,maxrow,maxcol)
        corresponding_quadrant = GetQuadrant(x,y,maxrow,maxcol)
        if corresponding_quadrant != -1:
            quadrant_population[corresponding_quadrant] += 1

    sfactor = quadrant_population[0]

    for quadrant in quadrant_population[1:]:
        sfactor = sfactor*quadrant

    return sfactor

def GetQuadrant(x_coord,y_coord,maxrow,maxcol):
    #1 = Q1, 2 = Q2, 3 = Q3, 4=Q4
    if maxrow%2== 0 and maxcol%2 ==0: #no middle
        if x_coord <= maxrow//2 and y_coord <= maxcol//2:
            return 1
        elif x_coord <= maxrow//2 and maxcol//2<y_coord:
            return 0
        elif maxrow//2< x_coord and y_coord <= maxcol//2:
            return 2
        else:
            return 3
    elif maxrow%2 != 0 and maxcol%2 ==0:#row middle
        if x_coord == maxrow//2:
            return -1
        if x_coord <= maxrow//2-1 and y_coord <= maxcol//2:
            return 1
        elif x_coord <= maxrow//2-1 and maxcol//2<y_coord:
            return 0
        elif maxrow//2< x_coord and y_coord <= maxcol//2:
            return 2
        else:
            return 3
    elif maxrow%2 == 0 and maxcol%2 != 0:#col middle
        if y_coord == maxcol//2:
            return -1
        if x_coord <= maxrow//2 and y_coord <= maxcol//2-1:
            return 1
        elif x_coord <= maxrow//2 and maxcol//2<y_coord:
            return 0
        elif maxrow//2< x_coord and y_coord <= maxcol//2-1:
            return 2
        else:
            return 3
    else:#row and col middle
        if x_coord == maxrow//2 or y_coord == maxcol//2:
            return -1
        elif x_coord <= maxrow//2-1 and y_coord <= maxcol//2-1:
            return 1
        elif x_coord <= maxrow//2-1 and maxcol//2<y_coord:
            return 0
        elif maxrow//2< x_coord and y_coord <= maxcol//2-1:
            return 2
        else:
            return 3



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
        guards[index] = (startpos,movement_vector)
        index += 1

    return guards

guard_info = TextToGuards('input.txt')
print(SafetyFactor(103,101,guard_info,100))
