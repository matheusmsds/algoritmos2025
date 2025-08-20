

def verificar_notas_abaixo_da_media(notas, nomes):
    soma = 0
    for i in range(0, len(notas)):
        soma += notas[i]
    media = soma / len(notas)
    
    
    # for i in range(0, len(nomes)):
    #     if(notas[i] < media):
    #         array[i] = nomes[i]

    # return array


notas = [7, 4, 9, 6, 5]
nomes = ["João", "Maria", "Pedro", "Ana", "Lucas"]

print(verificar_notas_abaixo_da_media(notas, nomes))