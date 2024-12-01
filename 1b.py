import mergesort as ms
similarity = 0
left, right = [], []
count = dict()


f = open('input.txt','r')
for line in f:
    temp = line.split()
    left.append(int(temp[0]))
    right.append(int(temp[1]))
f.close()

for number in right:
    if number in count.keys():
        count[number] += 1
    else:
        count[number] = 1
for number in left:
    if number in count.keys():
        similarity += number*count[number]

print(similarity)
