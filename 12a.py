def FencingPrice(map):
    total_price = 0
    m = len(map)
    n = len(map[0])

    for i in range(m):
        for j in range(n):
            if map[i][j] != " ":
                indices = ConnectPlot(map,i,j,set())
                total_price += len(indices) * Perimeter(map,indices)
                for index in indices:
                    map[index[0]][index[1]] = " "
    return total_price



def Perimeter(map,indices):
    """
    Returns the perimeter of a plot
    """
    surface = 0
    m = len(map)
    n = len(map[0])

    for i in range(m):
        for j in range(n):
            sub_indices = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for index in sub_indices:
                if (index[0],index[1]) not in indices:
                    if (i,j) in indices:
                        surface += 1

    return surface


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