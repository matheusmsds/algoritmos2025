array = [0] * 8
for i in range(0, len(array)):
    array[i] = random.randint(0, 100)

for i in range(0, len(array) - 1):
    for j in range(0, len(array) - 1):
        if(array[j] > array[j+1]):
            aux = array[j]
            array[j] = array[j+1]
            array[j+1] = aux

print(array)
