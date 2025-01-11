def TextToGridAndSequence(filenamestring):
    f = open(filenamestring,'r')
    grid = []
    sequence = []

    for line in f:
        if "#" in line:
            temp = list(line.rstrip())
            new_line = []
            for element in temp:
                if element == "#":
                    for i in range(2):
                        new_line.append("#")
                elif element == ".":
                    for i in range(2):
                        new_line.append(".")
                elif element == "O":
                    new_line.append("[")
                    new_line.append("]")
                elif element == "@":
                    new_line.append("@")
                    new_line.append(".")
            grid.append(new_line)

        else:
            temp = list(line.rstrip())

            for element in temp:
                if element == ">":
                    sequence.append([0,1])
                elif element == "<":
                    sequence.append([0,-1])
                elif element == "v":
                    sequence.append([1,0])
                else:
                    sequence.append([-1,0])

    return grid, sequence

def Display(grid):
    temp  = []
    for i in range(len(grid)):
        temp.append("".join(grid[i]))
    print(*temp,sep="\n")
def HorizontalPush(grid,position,vector):
    dx = vector[0]
    dy = vector[1]

    current_pos = [position[0]+dx,position[1]+dy]
    passed = [position]
    replacements = [".","@"]
    
    while True:
        if grid[current_pos[0]][current_pos[1]] == "#":
            break
        elif grid[current_pos[0]][current_pos[1]] in ["[","]"]:
            passed.append(current_pos)
            replacements.append(grid[current_pos[0]][current_pos[1]])
            current_pos = [current_pos[0]+dx,current_pos[1]+dy]

        elif grid[current_pos[0]][current_pos[1]] == ".":
            passed.append(current_pos)
            for i in range(len(passed)):
                grid[passed[i][0]][passed[i][1]] = replacements[i]
            position = [position[0]+dx,position[1]+dy]
            break        
        else:
            print("Push error")
            break
        
    return grid, position


def VerticalPush(grid,position,vector):
    original_position = list(position)
    dx = vector[0]
    dy = vector[1]
    passed = [position]
    current_position = [position[0]+dx,position[1]+dy]
    if grid[current_position[0]][current_position[1]] == ".":
        grid[position[0]][position[1]] = "."
        grid[current_position[0]][current_position[1]] = "@"
        return grid, current_position

    elif grid[current_position[0]][current_position[1]] == "[":
        current_positions = [(current_position[0],current_position[1]),(current_position[0],current_position[1]+1)]
        layers = [position for position in current_positions]
        last_positions = current_positions
        indices = set()
        for position in current_positions:
            indices.add(position)
        while True:
            current_positions = []
            for position in last_positions:
                if grid[position[0]+dx][position[1]] == "[":
                    current_positions.append([position[0]+dx,position[1]])
                    current_positions.append([position[0]+dx,position[1]+1])
                elif grid[position[0]+dx][position[1]] == "]":
                    current_positions.append([position[0]+dx,position[1]])
                    current_positions.append([position[0]+dx,position[1]-1])
                elif grid[position[0]+dx][position[1]] == "#":
                    return grid, original_position
                else:
                    current_position.append(position)
            if current_positions == last_positions:
                break
            else:
                last_positions = current_positions
                for position in current_positions:
                    indices.add((position[0],position[1]))
        layers = dict()
        keys = []
        for index in indices:
            if index[0] in layers:
                layers[index[0]].append(index)
            else:
                layers[index[0]] = [index]
                keys.append(index[0])
        if dx==1:
            keys = sorted(keys,reverse=True)
        else:
            keys = sorted(keys)
        for key in keys:
            for index in layers[key]:
                grid[index[0]+dx][index[1]] = grid[index[0]][index[1]]
                grid[index[0]][index[1]] = "."
        grid[original_position[0]][original_position[1]] = "."
        grid[original_position[0]+dx][original_position[1]] = "@"
        return grid, [original_position[0]+dx,original_position[1]]
    elif grid[current_position[0]][current_position[1]] == "]":
        current_positions = [(current_position[0],current_position[1]),(current_position[0],current_position[1]-1)]
        layers = [position for position in current_positions]
        last_positions = current_positions
        indices = set()
        for position in current_positions:
            indices.add(position)
        while True:
            current_positions = []
            for position in last_positions:
                if grid[position[0]+dx][position[1]] == "[":
                    current_positions.append([position[0]+dx,position[1]])
                    current_positions.append([position[0]+dx,position[1]+1])
                elif grid[position[0]+dx][position[1]] == "]":
                    current_positions.append([position[0]+dx,position[1]])
                    current_positions.append([position[0]+dx,position[1]-1])
                elif grid[position[0]+dx][position[1]] == "#":
                    return grid, original_position
                else:
                    current_positions.append(position)
            if current_positions == last_positions:
                break
            else:
                last_positions = current_positions
                for position in current_positions:
                    indices.add((position[0],position[1]))
        layers = dict()
        keys = []
        for index in indices:
            if index[0] in layers:
                layers[index[0]].append(index)
            else:
                layers[index[0]] = [index]
                keys.append(index[0])
        if dx==1:
            keys = sorted(keys,reverse=True)
        else:
            keys = sorted(keys)
        for key in keys:
            for index in layers[key]:
                grid[index[0]+dx][index[1]] = grid[index[0]][index[1]]
                grid[index[0]][index[1]] = "."
        grid[original_position[0]][original_position[1]] = "."
        grid[original_position[0]+dx][original_position[1]] = "@"
        return grid, [original_position[0]+dx,original_position[1]]
    else:
        return grid, original_position
                
def ExecuteMovements(grid,movement_sequence,starting_position):

    x_coord = starting_position[0]
    y_coord = starting_position[1]
    for vector in movement_sequence:
        if vector in [[0,1],[0,-1]]:
            grid, position = HorizontalPush(grid,[x_coord,y_coord],vector)
            x_coord = position[0]
            y_coord = position[1]
        else:
            grid,position = VerticalPush(grid,[x_coord,y_coord],vector)
            x_coord = position[0]
            y_coord = position[1]
    return grid
        
def GetRobotCoords(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return [i,j]
            
def EvaluateGrid(grid):
    score = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                score += 100*i + j

    print(score)
grid, sequence = TextToGridAndSequence('input.txt')
EvaluateGrid(ExecuteMovements(grid,sequence,GetRobotCoords(grid)))