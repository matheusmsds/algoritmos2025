array = [32, 9, 12, 3, 68, 27,15]

for i in range(0, len(array) - 1):
    for j in range(0, len(array) - 1):
        if(array[j] > array[j+1]):
            aux = array[j]
            array[j] = array[j+1]
            array[j+1] = aux

print(array)
