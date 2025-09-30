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
        menor_valor = array[i]
        imenor = i
        for j in range(i+1, len(array)):
            if(array[j] < menor_valor):
                menor_valor = array[j]
                imenor = j

                array[imenor] = array[i]
                array[i] = menor_valor
            
    return array

def busca_sequencial(array, valor):
    indice = None
    for i in range(len(array)):
        if(valor == array[i]):
            indice = i
            break

    if(indice is None):
        return -1
    else:
        return indice

# O(log2 n)
def busca_binaria(array, valor):
    selection_sort(array)  # garantir que está ordenado

    indice = None
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if(array[meio] == valor):
            indice = meio
            break
        elif(array[meio] > valor):
            fim = meio - 1
        else:
            inicio = meio + 1

    if(indice is None):
        return -1
    else:
        return indice


def criar_vetor(tam, variacao_x, variacao_y):
    vetor = [0] * tam
    for i in range(0, tam):
        vetor[i] = random.random(variacao_x, variacao_y)
    

    return vetor

