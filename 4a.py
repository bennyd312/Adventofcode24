def CeresSearch(text):
    n = len(text[0]) #number of columns
    m = len(text) #number of rows
    count = 0
    print(m,n)
    for i in range(m):
        for j in range(n):
            if text[i][j] != "0":
                count += FullSearch(text,i,j)
    return count
def FullSearch(text,i,j):
    total = 0
    total += LeftHorizontalSearch(text,i,j)
    total += RightHorizontalSearch(text,i,j)
    total += UpperVerticalSearch(text,i,j)
    total += LowerVerticalSearch(text,i,j)
    total += FirstDiagonalSearch(text,i,j)
    total += SecondDiagonalSearch(text,i,j)
    total += FirstAntidiagonalSearch(text,i,j)
    total += SecondAntidiagonalSearch(text,i,j)
    return total
def LeftHorizontalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i][j-1] == word[1]:
            if text[i][j-2] == word[2]:
                if text[i][j-3] == word[3]:
                    return 1
    return 0
def RightHorizontalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i][j+1] == word[1]:
            if text[i][j+2] == word[2]:
                if text[i][j+3] == word[3]:
                    return 1
    return 0

def UpperVerticalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i-1][j] == word[1]:
            if text[i-2][j] == word[2]:
                if text[i-3][j] == word[3]:
                    return 1
    return 0
def LowerVerticalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i+1][j] == word[1]:
            if text[i+2][j] == word[2]:
                if text[i+3][j] == word[3]:
                    return 1
    return 0
def FirstDiagonalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i-1][j-1] == word[1]:
            if text[i-2][j-2] == word[2]:
                if text[i-3][j-3] == word[3]:
                    return 1
    return 0
def SecondDiagonalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i+1][j+1] == word[1]:
            if text[i+2][j+2] == word[2]:
                if text[i+3][j+3] == word[3]:
                    return 1
    return 0
def FirstAntidiagonalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i+1][j-1] == word[1]:
            if text[i+2][j-2] == word[2]:
                if text[i+3][j-3] == word[3]:
                    return 1
    return 0
def SecondAntidiagonalSearch(text,i,j):
    word = ['X','M','A','S']

    if text[i][j] == word[0]:
        if text[i-1][j+1] == word[1]:
            if text[i-2][j+2] == word[2]:
                if text[i-3][j+3] == word[3]:
                    return 1
    return 0
def AddPadding(text):
    row = len(text)
    col = len(text[0])
    updated = []
    temp = "000000"
    for i in range(col):
        temp += "0"
    for i in range(3):
        updated.append(temp)
    
    for i in range(row):
        temp1 = "000"
        temp1 += text[i]
        temp1 += "000"
        updated.append(temp1)
    for i in range(3):
        updated.append(temp)
    
    return updated

                
text = []
f = open('input.txt','r')
for line in f:
    text.append(line.strip())
f.close()

print(CeresSearch(AddPadding(text)))