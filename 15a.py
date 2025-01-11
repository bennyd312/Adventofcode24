def EvaluateGrid(grid):
    score = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                score += 100*i + j

    print(score)


def ExecuteMovements(grid,movement_sequence,starting_position):

    x_coord = starting_position[0]
    y_coord = starting_position[1]

    for vector in movement_sequence:
        grid, position = Push(grid,[x_coord,y_coord],vector)
        x_coord = position[0]
        y_coord = position[1]

    temp  = []
    for i in range(len(grid)):
        temp.append("".join(grid[i]))
        
    return grid


def Push(grid,position,vector):
    dx = vector[0]
    dy = vector[1]

    current_pos = [position[0]+dx,position[1]+dy]
    passed = [position]
    replacements = [".","@"]
    
    while True:
        if grid[current_pos[0]][current_pos[1]] == "#":
            break
        elif grid[current_pos[0]][current_pos[1]] == "O":
            passed.append(current_pos)
            replacements.append("O")
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
def GetRobotCoords(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return [i,j]
            
def TextToGridAndSequence(filenamestring):
    f = open(filenamestring,'r')
    grid = []
    sequence = []

    for line in f:
        if "#" in line:
            grid.append(list(line.rstrip()))
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

grid, sequence = TextToGridAndSequence('input.txt')
EvaluateGrid(ExecuteMovements(grid,sequence,GetRobotCoords(grid)))