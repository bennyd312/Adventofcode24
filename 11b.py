def PlutoPebbles(sequence,blinks):
    storage = {rock:1 for rock in sequence}
    temp_storage = dict()
    index = 0
    temp_sequence = sequence
    count = 0

    while index<blinks:

        for rock in set(temp_sequence):
            temp = Blink(rock)
            for pebble in temp:
                if pebble in temp_storage.keys():
                    temp_storage[pebble] += storage[rock]
                else:
                    temp_storage[pebble] = storage[rock]
    
        storage = temp_storage
        temp_sequence = storage.keys()
        temp_storage = dict()
        index += 1

    for rock in storage.keys():
        count += storage[rock]

    return count

def Blink(number):

    if number == "0":
        return ["1"]
    
    elif len(number)%2==0:
        return [Prune(number[:(len(number)//2)]),Prune(number[(len(number)//2):])]
    else:

        return [str(int(number)*2024)]
    
def Prune(number):
    return str(int(number))

def TextToSequence(filenamestring):
    sequence = []
    f = open(filenamestring,'r')
    for line in f:
        stripped_line = list(line.rstrip().split())
        for element in stripped_line:
            sequence.append(element)

    f.close()

    return sequence

sequence = TextToSequence('input.txt')
print(PlutoPebbles(sequence,75))
