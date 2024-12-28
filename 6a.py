def AddPadding(text):
    row = len(text)
    col = len(text[0])
    updated = []
    temp = "0"
    for i in range(col):
        temp += "0"
    for i in range(1):
        updated.append(temp)
    
    for i in range(row):
        temp1 = "0"
        temp1 += text[i]
        temp1 += "0"
        updated.append(temp1)
    for i in range(1):
        updated.append(temp)
    
    updated_result = [list(line) for line in updated]

    return updated_result
def FindGuard(text):
    row = len(text)
    col = len(text[0])
    guardrow, guardcol  = 0, 0
    found = False

    for i in range(row):
        if found == False:
            for j in range(col):
                if text[i][j] in ['<','>','^','v']:
                    guardrow, guardcol = i, j
                    found = True
                    break
        else:
            break
    return guardrow, guardcol
def GuardRoute(text):
    count = 1
    guardrow, guardcol = FindGuard(text)
    direction = None
    guard = text[guardrow][guardcol]
 
    if guard == "^":
        direction = "up"
    elif guard == ">":
        direction = "right"
    elif guard == "v":
        direction = "down"
    else:
        direction = "left"

    print(text[guardrow][guardcol])
    text[guardrow][guardcol] = "X"

    while True:
        if direction == "up":
            nextrow = guardrow-1
            nextcol = guardcol
            if text[nextrow][nextcol] == "0":
                return count
            elif text[nextrow][nextcol] == "#":
                direction = "right"
            elif text[nextrow][nextcol] == ".":
                text[nextrow][nextcol] = "X"
                count += 1
                guardrow = nextrow
            else:
                guardrow = nextrow

        elif direction == "right":
            nextrow = guardrow
            nextcol = guardcol+1
            if text[nextrow][nextcol] == "0":
                return count
            elif text[nextrow][nextcol] == "#":
                direction = "down"
            elif text[nextrow][nextcol] == ".":
                text[nextrow][nextcol] = "X"
                count += 1
                guardcol = nextcol
            else:
                guardcol = nextcol


        elif direction == "down":
            nextrow = guardrow+1
            nextcol = guardcol
            if text[nextrow][nextcol] == "0":
                return count
            elif text[nextrow][nextcol] == "#":
                direction = "left"
            elif text[nextrow][nextcol] == ".":
                text[nextrow][nextcol] = "X"
                count += 1
                guardrow = nextrow
            else:
                guardrow = nextrow

        elif direction == "left":
            nextrow = guardrow
            nextcol = guardcol - 1
            if text[nextrow][nextcol] == "0":
                return count
            elif text[nextrow][nextcol] == "#":
                direction = "up"
            elif text[nextrow][nextcol] == ".":
                text[nextrow][nextcol] = "X"
                count += 1
                guardcol = nextcol
            else:
                guardcol = nextcol


    

text = []
f = open('input.txt','r')
for line in f:
    text.append(line.strip())
f.close()

print(GuardRoute(AddPadding(text)))
