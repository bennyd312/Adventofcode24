#Oriented graph

class vertex():
    def __init__(self,node,outgoing = []):
        self.node = node
        self.outgoing = outgoing

def CheckSequence(sequence,graph):
    n = len(sequence)
    for i in range(0,n-1):
        for j in range(i,n):
            if sequence[j] in graph.keys():
                if sequence[i] in graph[sequence[j]].outgoing:
                    return False
    return True





rules = [] #(x|y) -> (x,y) tuple
sequences = [] # (1,2,3,6)... sequences to check

f = open('input.txt','r')
switch = False
for line in f:
    temp = line.rstrip()
    if temp == "":
        switch = True
    elif switch == False:
        temp = temp.split(sep="|")
        rules.append((int(temp[0]),int(temp[1])))
    else:
        temp = temp.split(sep=",")
        sequence = [int(num) for num in temp]
        sequences.append(sequence)
f.close()


total = 0
graph = dict()
knownvertices = []
for rule in rules:
    start = rule[0]
    end = rule[1]
    if start not in knownvertices:
        graph[start] = vertex(start,[end])
        knownvertices.append(start)
    else:
        graph[start].outgoing.append(end)

for sequence in sequences:
    if CheckSequence(sequence,graph) == True:
        print(sequence)
        n = len(sequence)-1
        middle = sequence[n//2]
        total += middle

print(total)