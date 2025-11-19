def criarLista():
    lista = []
    return lista

def preencherLista(lista:list, valor_saida):
    i = 0
    while(True):
        i += 1
        valor = int(input(f"Informe {i}º valor: "))
        if(valor == valor_saida):
            break
        else:
            lista.append(valor)

def valorPresente(lista:list, valor):
    presente = False
    for i in range(0, len(lista)):
        if(lista[i] == valor):
            presente = True
    return presente

def menorValor(lista:list):
    for i in range(0, len(lista)):
        if(i == 0):
            menor_valor = lista[i]
        if(lista[i] < menor_valor):
            menor_valor = lista[i]
    return menor_valor

def removerDuplicatas(lista:list):
    temp = []
    for i in range(0, len(lista)):
        if(lista[i] not in temp):
            temp.append(lista[i])
    lista.clear()
    
    for i in range(0, len(temp)):
        lista.append(temp[i])

def main():
    lista = criarLista()
    preencherLista(lista, 90)
    valor = 20
    presente = valorPresente(lista, valor)
    menor_valor = menorValor(lista)
    remover_rep = removerDuplicatas(lista)
    if(presente):
        print(f"{valor} está presente nesta lista.")
    else:
        print(f"{valor} não está presente nesta lista.")

    print(f"O menor valor da lista é: {menor_valor}")
    print()
    for elemento in lista:
        print(elemento)

main()