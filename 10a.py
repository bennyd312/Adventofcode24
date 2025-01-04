map = [[0,3,0],
       [1,5,9],
       [2,9,8],
       [3,8,7],
       [4,5,6]]

def EvaluateMap(map):
    m = len(map)
    n = len(map[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if map[i][j] == 0:
                count += len(trailhead_score(map,i,j))
    
    return count

def trailhead_score(map,i,j):
    """
    Recursive functions
    Initial input: map[i][j] == 0
    Recursively seeks in every direction to increase the elevation by 1 until it reaches 9.
    Output: set of all reachable peaks
    """
    peaks = set()

    if map[i][j] == 9:
        peaks.add((i,j))
    else:
        indices = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
        for index in indices:
            try:
                conditions = [index[0] in range(len(map)),
                            index[1] in range(len(map[0])),
                            map[index[0]][index[1]]==map[i][j]+1]
                if all(conditions):
                    next_path = trailhead_score(map,index[0],index[1])
                    for peak in next_path:
                        peaks.add(peak)
            except IndexError:
                continue
    return peaks

def TextToMap(filenamestring):
    map = []
    f = open(filenamestring,'r')
    for line in f:
        stripped_line = list(line.rstrip())
        map.append([int(element) for element in stripped_line])

    f.close()

    return map
map = TextToMap('input.txt')
print(EvaluateMap(map))