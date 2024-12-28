import copy
def CheckEquality(number,sequence):
    OperationSequences = TernaryPermutations(len(sequence)-1)

    for oseq in OperationSequences:
        temp = copy.deepcopy(sequence)
        for i in range(len(sequence)-1):
            if oseq[i] == 0:
                temp[i+1] = temp[i] * temp[i+1]
                temp[i] = 0
            elif oseq[i]==1:
                concat = str(temp[i]) + str(temp[i+1])
                temp[i] = 0
                temp[i+1] = int(concat)
            else:
                temp[i+1] = temp[i] + temp[i+1]
                temp[i] = 0
        total = sum(temp)
        if total == number:
            return True
    return False
    
def TernaryPermutations(number):
    permutations = []
    i = 0

    while i<=(3**number)-1:
        permutation = NumberToTernary(i,number)
        if len(permutation)<number:
            diff = number - len(permutation)
            temp = []
            for k in range(diff):
                temp.append(0)
            for j in permutation:
                temp.append(j)
            permutations.append(temp)
        else:
            permutations.append(permutation)
        i+=1

    return permutations


def NumberToTernary(number,length):

    exp = 0
    binary = []
    remainder = number
    while True:
        if number>=3**(exp+1):
            exp+=1
        else:
            break

    while exp>-1:
        whole = remainder//(3**exp)
        exp = exp - 1
        if whole!=0:
            remainder = remainder - whole*3**(exp+1)
            binary.append(whole)
        else:
            binary.append(0)

    binaryfinal = []
    if len(binary)<length:
        diff = length - len(binary)
        for k in range(diff):
            binaryfinal.append(0)
        for element in binary:
            binaryfinal.append(element)
        return binaryfinal
    else:
        return binary


equationsrhs = []
equationslhs = []
f = open('input.txt','r')

for line in f:
    temp = line.strip()
    temp = temp.split()
    number = int(temp[0][:-1])
    sequence = []
    for i in range(1,len(temp)):
        sequence.append(int(temp[i]))

    equationslhs.append(number)
    equationsrhs.append(sequence)
f.close()
total = 0


for i in range(len(equationslhs)):
    if CheckEquality(equationslhs[i],equationsrhs[i])==True:
        total += equationslhs[i]

print(total)
