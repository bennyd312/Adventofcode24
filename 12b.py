def FencingPrice(map):
    total_price = 0
    m = len(map)
    n = len(map[0])

    for i in range(m):
        for j in range(n):
            if map[i][j] != " ":
                indices = ConnectPlot(map,i,j,set())
                total_price += len(indices) * CountSides(map,indices)
                for index in indices:
                    map[index[0]][index[1]] = " "
    return total_price

def ConstructSides(map,indices):
    """
    Input: indices of fenced area
    Ouput: Dict containing the fenced sides of each index tile
    """
    m = len(map)
    n = len(map[0])
    temp_map = [[False for j in range(n) ] for i in range(m)]
    fences = {index : set() for index in indices}

    for index in indices:
        temp_map[index[0]][index[1]] = True
        sub_indices = [(index[0]+1,index[1]),(index[0]-1,index[1]),(index[0],index[1]+1),(index[0],index[1]-1)]
        for sub_index in sub_indices:
            if sub_index[0] in range(m) and sub_index[1] in range(n):
                if temp_map[sub_index[0]][sub_index[1]] == False:
                    fences[index].add(GetDirection(index,sub_index))
                else:
                    fences[sub_index].remove(GetDirection(sub_index,index))
            else:
                fences[index].add(GetDirection(index,sub_index))
    return fences
def GetDirection(index,sub_index):
    if index[0]<sub_index[0]:
        return "right"
    elif index[0]>sub_index[0]:
        return "left"
    elif index[1]<sub_index[1]:
        return "up"
                            
    else:
        return "down"
    
def CountSides(map,indices):
    """
    returns the number of sides in a map
    """
    sides = 0
    fences = ConstructSides(map,indices)
    for index in indices:
        directions = fences[index]
        traversed = []
        for direction in directions:
            if direction == "right" or direction =="left":
                i,j = index[0], index[1]
                while True: # go left
                    try:
                        if direction in fences[(i,j+1)]:
                            traversed.append((i,j+1))
                            j += 1
                        else:
                            break
                    except KeyError:
                        break
                i,j = index[0], index[1]
                while True: #go right
                    try:
                        if direction in fences[(i,j-1)]:
                            traversed.append((i,j-1))
                            j += -1
                        else:
                            break
                    except KeyError:
                        break
                for sub_index in traversed:
                    fences[sub_index].remove(direction)
                sides += 1
                traversed = []
            else:
                i,j = index[0], index[1]
                while True: # go down
                    try:
                        if direction in fences[(i+1,j)]:
                            traversed.append((i+1,j))
                            i += 1
                        else:
                            break
                    except KeyError:
                        break
                i,j = index[0], index[1]
                while True: #go right
                    try:
                        if direction in fences[(i-1,j)]:
                            traversed.append((i-1,j))
                            i += -1
                        else:
                            break
                    except KeyError:
                        break
                for sub_index in traversed:
                    fences[sub_index].remove(direction)
                sides += 1
                traversed = []
        fences[index] = []
    print(sides)
    return sides
def ConnectPlot(map,startrow,startcol,indices):
    """
    Input: Initial coordinates
    Output: Coordinates of the fenced plot
    """
    indices.add((startrow,startcol))

    search_indices = [(startrow+1,startcol),(startrow-1,startcol),(startrow,startcol+1),(startrow,startcol-1)]

    for index in search_indices:
        if index[0] in range(len(map)) and index[1] in range(len(map[0])) and (index[0],index[1]) not in indices:
            if map[index[0]][index[1]] == map[startrow][startcol]:
                indices.add((index[0],index[1]))
                new_search_indices = ConnectPlot(map,index[0],index[1],indices)
                for new_index in new_search_indices:
                    indices.add(new_index)

    
    return indices

def TextToMap(filenamestring):
    sequence = []
    f = open(filenamestring,'r')
    for line in f:
        stripped_line = list(line.rstrip())
        sequence.append(stripped_line)

    f.close()

    return sequence

print(FencingPrice(TextToMap('input.txt')))