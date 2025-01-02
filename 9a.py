def Convert_Diskmap_to_sequence(diskmap):
    """
    Converts a diskmap, ie numbers "12345" to [0,.,.,1,1,1,.,.,.,.,2,2,2,2,2] (a sequence)
    """
    n = len(diskmap)
    IDS = [] #id's used
    freespace_indices = [] #indices of dots / freespace
    C = [] # sequence without dots
    sequence = [] #final sequence
    id_blocks = []

    index = 0
    current_id = 0
    sequence_length = 0

    while index<n:
        if index%2==0:
            IDS.append(current_id)
            for j in range(diskmap[index]):
                id_blocks.append(current_id)
                sequence.append(current_id)
                C.append(current_id)
                sequence_length += 1
            current_id += 1
            index += 1
        else:
            for j in range(diskmap[index]):
                id_blocks.append(current_id)
                sequence.append(-1)
                freespace_indices.append(sequence_length)
                sequence_length += 1
            index += 1
    return sequence,freespace_indices,C,id_blocks

def Convert_Sequence_to_Files(sequence,freespace_indices,sequence_stripped):
    A = sequence
    B = freespace_indices
    C = sequence_stripped

    for index in freespace_indices:
        A[index] = C[-1]
        C.pop()
    for i in range(1,len(freespace_indices)+1):
        A[-i]=-1

    return A

def ComputeChecksum(sequence,id_blocks):
    checksum = 0
    for i in range(len(sequence)):
        if sequence[i] != -1:
            checksum += i*sequence[i]

    return checksum

def TextToDiskmap(filenamestring):
    diskmap = []
    f = open(filenamestring,'r')
    for line in f:
        temp = list(line.rstrip())
        for element in temp:
            diskmap.append(int(element))


    f.close()

    return diskmap

diskmap = TextToDiskmap('input.txt')
sequence,freespace_indices,C,id_blocks = Convert_Diskmap_to_sequence(diskmap)
new_sequence = Convert_Sequence_to_Files(sequence,freespace_indices,C)
print(ComputeChecksum(new_sequence,id_blocks))
