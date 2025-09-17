import random

def bubble_sort(array):
    for ciclo in range(0, len(array) - 1):
        for i in range(0, len(array) - 1):
            if(array[i] > array[i+1]):
                aux = array[i]
                array[i] = array[i+1]
                array[i+1] = aux
    return array

def insert_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while(j >= 0 and temp < array[j]):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array

def selection_sort(array):
    for i in range(0, len(array) -1):
        menor = array[i]
        imenor = i
        for j in range(i+1, len(array)):
            if(array[j] < menor):
                menor = array[j]
                imenor = j

        array[imenor] = array[i]
        array[i] = menor
            
    return array


tam = int(input("Informe o tamanho do vetor: "))
array = [0] * tam

for i in range(0, len(array)):
    array[i] = random.randint(1, 100)

a = selection_sort(array)
print(a)