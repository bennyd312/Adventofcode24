"""
non-recursive mergesort

sorts the list by splitting it into pair blocks and iteratively merging them

for each block pair we are indexing separately over each block from first index (smallest element in each block)
for each pair of elements of given indices we compare them and add the smaller one to a new list
the index of the smaller value is raised by one. If we run out of index, we simply add all the leftover elements from the other list to the new list.
"""

def merge(elements1,elements2):
    n , m= len(elements1) , len(elements2)
    i , j = 0 , 0
    new = []
    while i<=n-1 and j<=m-1:
        if elements1[i]<=elements2[j]:
            new.append(elements1[i])
            i += 1
        else:
            new.append(elements2[j])
            j += 1
    while i<=n-1:
        new.append(elements1[i])
        i+=1

    while j<=m-1:
        new.append(elements2[j])
        j+=1

    return new


def mergesort(elements):
    b = 1
    n = len(elements)

    while b<n:
        i = 0
        j = b

        while j<=n:
            k = min(j+b-1,n-1)
            X = elements[i:j]
            Y = elements[j:k+1]
            temp = merge(X,Y)
            elements[i:k+1] = temp
            i = i + 2*b
            j = j + 2*b
        b = 2*b
    
    return elements