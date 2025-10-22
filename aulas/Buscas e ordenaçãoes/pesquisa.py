# busca linear / pesquisa sequencial

def busca_nao_ordenada(array, valor):
    encontrei = False
    indice = None
    for i in range(0, len(array)):
        if(valor == array[i]):
            encontrei = True
            indice = i
            break

    if(encontrei):
        print(f"O valor {valor} está na posição {indice}")
    else:
        print(f"O valor {valor} não está no vetor")

def busca_ordenada(array,valor):
    encontrei = False
    indice = None
    for i in range(0, len(array)):
        if(valor < array[i]):
            encontrei = True
            indice = i
            break

        if(encontrei):
            print(f"O valor {valor} está na posição {indice}")
        else:
            print(f"O valor {valor} não está no vetor")

#//////////// busca binaria
# meio = int((inicio + fim) / 2)
# inicio = meio + 1
# fim = meio - 1
# inicio, meio e fim são indices!

def busca_binaria(array, valor):
    encontrei = False
    indice = None
    inicio = 0
    fim = len(array) - 1
    
    while(inicio <= fim):
        meio = int((inicio + fim) / 2)

        if(array[meio] == valor):
            encontrei = True
            indice = meio
            break
        elif(array[meio] > valor):
            fim = meio - 1
        else:
            inicio = meio + 1

    if(encontrei):
        print(f"O valor {valor} está na posição {indice}")
    else:
        print(f"O valor {valor} não está no vetor")

array = [1,3,5,7,10,12,15]
valor = int(input("Informe um número: "))

busca_binaria(array,valor)