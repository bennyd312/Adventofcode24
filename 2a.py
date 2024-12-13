
def SafetyCheck(sequence):
    safety = True
    increasing = None
    states = dict()
    
    if sequence[1]-sequence[0]>0:
        monotone = True
    elif sequence[1]-sequence[0]<0:
        monotone = False
    else:
        safety = False


    for i in range(len(sequence)-1):
        difference = sequence[i+1] - sequence[i]
        if abs(difference)>0 and abs(difference)<4:
            if difference>0:
                states[True] = 0
            elif difference<0:
                states[False] = 0
            else:
                states[None] = 0
        else:
            safety = False
            return safety
        

    if len(states.keys())==1:
        return safety
    else:
        safety = False
        return safety

def StringToSequence(line):
    sequence = [int(i) for i in line.split()]
    return sequence


count = 0


f = open('input.txt','r')
for line in f:
    if SafetyCheck(StringToSequence(line)) == True:
        count+=1
f.close()

print(count)
