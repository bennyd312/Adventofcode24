def PlutoPebbles(sequence,blinks):
    output_sequence = []
    for number in sequence:
        temp_sequence = [number]
        while_sequence = []
        index = 0
        while index<blinks:
            for element in temp_sequence:
                result = Blink(element)
                for item in result:
                    while_sequence.append(item)
                
            temp_sequence = while_sequence
            while_sequence = []
            index += 1
        for element in temp_sequence:
            output_sequence.append(element)
    return len(output_sequence) #we desire only the number of pebbles

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
print(PlutoPebbles(sequence,25))