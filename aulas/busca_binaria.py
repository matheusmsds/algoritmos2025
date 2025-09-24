def busca_binaria(array, valor):
    indice = None
    inicio = 0
    fim = len(array) - 1
    
    while(inicio <= fim):
        meio = int((inicio + fim) / 2)

        if(array[meio] == valor):
            indice = meio
            break
        elif(array[meio] > valor):
            fim = meio - 1
        else:
            inicio = meio + 1

    return indice
