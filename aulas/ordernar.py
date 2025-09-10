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

array = [32,9,12,3,68,27,15]
for i in range(0, len(array) - 1):
    for j in range(0,len(array) - 1):
        if(array[j] > array[j+1]):
            aux = array[j]
            array[j] = array[j+1]
            array[j+1] = aux
    print(f"Fim do {j + 1} ciclo: {array}")

array = [32,9,12,3,68,27,15]
def bubble(vetor):
    for ciclo in range(0, len(vetor) - 1):
        for i in range(0,len(vetor) - 1):
            if(vetor[i] > vetor[i+1]):
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux
    return vetor

print(bubble(array))
