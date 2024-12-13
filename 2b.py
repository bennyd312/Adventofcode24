def SafetyCheck(sequence):
    safety = True
    increasing1 = sequence[1] - sequence[0]
    increasing2 = sequence[len(sequence)-1] - sequence[len(sequence)-2]
    states = dict()
    
    if increasing1>0 and increasing2>0:
            monotone = True

    elif increasing1<0 and increasing2<0:
            monotone = False
    else:
        return False


    for i in range(len(sequence)-1):
        difference = sequence[i+1] - sequence[i]
        if abs(difference)>0 and abs(difference)<4:
            if difference>0 and monotone==False:
                return False
            elif difference<0 and monotone==True:
                return False

        else:
            return False
    
    return True

def ReduceSequence(sequence,index):
    tempsequence = sequence[:index]
    for element in sequence[index+1:]:
        tempsequence.append(element)

    return tempsequence

def DampenerSafetyCheck(sequence):
    safety = True
    increasing1 = sequence[1] - sequence[0]
    increasing2 = sequence[len(sequence)-1] - sequence[len(sequence)-2]
    states = dict()
    monotone = None

    if increasing1>0 and increasing2>0:
            monotone = True

    elif increasing1<0 and increasing2<0:
            monotone = False


    else:
        increasing1 = sequence[2] - sequence[1]
        increasing2 = sequence[len(sequence)-2] - sequence[len(sequence)-3]

        if increasing1>0 and increasing2>0:
            monotone = True
        elif increasing1<0 and increasing2<0:
            monotone = False
        else:
             return False

    for i in range(len(sequence)-1):
        difference = sequence[i+1] - sequence[i]
        if abs(difference)>0 and abs(difference)<4:
            if difference>0 and monotone!= True:
                if True in [SafetyCheck(ReduceSequence(sequence,i+1)),SafetyCheck(ReduceSequence(sequence,i))]:
                     return True
                else:
                     return False

            elif difference<0 and monotone==True:
                if True in [SafetyCheck(ReduceSequence(sequence,i+1)),SafetyCheck(ReduceSequence(sequence,i))]:
                     return True
                else:
                     return False

            elif difference==0:
                if True in [SafetyCheck(ReduceSequence(sequence,i+1)),SafetyCheck(ReduceSequence(sequence,i))]:
                     return True
                else:
                     return False
        else:

            if True in [SafetyCheck(ReduceSequence(sequence,i+1)),SafetyCheck(ReduceSequence(sequence,i))]:
                 return True
            else:
                 return False
        

    return True

def StringToSequence(line):
    sequence = [int(i) for i in line.split()]
    return sequence




count = 0

print(DampenerSafetyCheck(StringToSequence("11 11 14 16 17")))


f = open('input.txt','r')
for line in f:
    if DampenerSafetyCheck(StringToSequence(line)) == True:
        count+=1
f.close()

print(count)

