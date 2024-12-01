import mergesort as ms
distance = 0
left, right = [], []

f = open('input.txt','r')
for line in f:
    temp = line.split()
    left.append(int(temp[0]))
    right.append(int(temp[1]))
f.close()

left_sorted, right_sorted = ms.mergesort(left), ms.mergesort(right)

for i in range(len(left_sorted)):
    distance += abs(left_sorted[i] - right_sorted[i])

print(distance)
