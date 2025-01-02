def Convert_Diskmap_to_sequence(diskmap):
    """
    Converts a diskmap, ie numbers "12345" to [0,.,.,1,1,1,.,.,.,.,2,2,2,2,2] (a sequence)
    """
    n = len(diskmap)
    IDS = [] #id's used
    freespace_indices = [] #indices of dots / freespace
    sequence_stripped_indices = []
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
                sequence_stripped_indices.append(sequence_length)
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
    return sequence,freespace_indices,C,id_blocks,sequence_stripped_indices

def Convert_Sequence_to_Files(sequence,sequence_stripped,sequence_stripped_indices):
    index = 0
    n = len(sequence)

    while index<n:
        temp_index = index
        freespace_startindex = 0
        freespace_count = 0
        j=1
        found = False
        while True:
            try:
                if sequence_stripped[-j-1] == sequence_stripped[-1]:
                    j+=1
                else:
                    break
            except IndexError:
                break
        while temp_index < n:
            if sequence_stripped == []:
                found = True
                break
            elif freespace_count == j:
                if freespace_startindex>sequence_stripped_indices[-j]:
                    break
                else:
                    for k in range(j):
                        sequence[freespace_startindex+k] = sequence_stripped[-1]
                        sequence[sequence_stripped_indices[-1]] = -1
                        sequence_stripped_indices.pop()
                        sequence_stripped.pop()
                    found = True
                    break
            elif sequence[temp_index] == -1:
                if freespace_startindex == 0:
                    freespace_startindex = temp_index
                    freespace_count += 1
                else:
                    freespace_count += 1
                temp_index += 1
            else:
                freespace_count = 0
                freespace_startindex = 0
                temp_index += 1
        if found == False:
            for k in range(j):
                sequence_stripped.pop()
                sequence_stripped_indices.pop()
        index += 1
    return sequence

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
sequence,freespace_indices,C,id_blocks,sequence_stripped_indices = Convert_Diskmap_to_sequence(diskmap)
new_sequence = Convert_Sequence_to_Files(sequence,C,sequence_stripped_indices)
print(ComputeChecksum(new_sequence,id_blocks))
