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

def textsearch(text):
    row = len(text)
    col = len(text[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if text[i][j] =="A":
                count += masSearch(text,i,j)
                pass
    
    return count

def masSearch(text,i,j):
    word = ['M','S']
    indices = [(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    temp = {'M': 0,
            'S': 0}
    for index in indices:
        letter = text[index[0]][index[1]] 
        if letter == 'S' or letter =='M':
            temp[letter] += 1
    if temp["M"] == 2 and temp['S'] == 2:
        index1 = indices[0]
        index2 = indices[3]
        letter1 = text[index1[0]][index1[1]]
        letter2 = text[index2[0]][index2[1]]
        if letter1 != letter2:
            return 1
        else:
            return 0
    else:
        return 0

text = []
f = open('input.txt','r')
for line in f:
    text.append(line.strip())
f.close()

print(textsearch(AddPadding(text)))