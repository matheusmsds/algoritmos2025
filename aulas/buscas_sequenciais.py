def busca_sequencial_nao_ordenada(array, valor):
    indice = None
    for i in range(0, len(array)):
        if(valor == array[i]):
            indice = i
            break

    return indice

def busca_sequencial_ordenada(array,valor):
    array = insert_sort(array)
    indice = None
    for i in range(0, len(array)):
        if(valor < array[i]):
            indice = i
            break

    return indice
