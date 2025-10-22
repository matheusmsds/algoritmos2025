# 1) Controle de Estoque de Frutas
# Uma quitanda precisa registrar o preço de 6 tipos de frutas que são atualizados todas as manhãs.
# a) Crie um vetor de ponto-flutuante chamado precosFrutas com 6 posições, inicializado com 0.0.
# precosFrutras = [0.0] * 6
# # b) Solicite ao funcionário que digite o preço de cada fruta (use o mesmo vetor para armazenar).
# for i in range(0, len(precosFrutras)):
#     precosFrutras[i] = float(input(f"Informe o preço do {i + 1}º item: "))
# # c) Após o preenchimento, exiba na tela todos os preços na mesma ordem em que foram digitados.
# for i in range(0, len(precosFrutras)):
#     print(f"fruta {i + 1} - R$ {precosFrutras[i]}")


# 2) Monitoramento Automático de Temperatura em um Laboratório
# Um laboratório de química registra automaticamente a temperatura ambiente a cada hora, durante 24 horas consecutivas, para garantir a estabilidade dos experimentos.
#a) Crie um vetor de inteiros chamado temperaturas com 24 posições, inicializado com 0.
# temperaturas = [0] * 24
# # b) Preencha o vetor sorteando valores inteiros entre 15 °C e 30 °C (inclusive).
# import random
# for i in range(0, len(temperaturas)):
#     temperaturas[i] = random.randint(15, 30)
# # c) Calcule e mostre:
# for i in range(0, len(temperaturas)):
#     print(f"Temperatura na posição {i + 1} - {temperaturas[i]}°C")
# # • A temperatura média do dia.
# # soma = 0
# # for i in range(0, len(temperaturas)):
# #     soma += temperaturas[i]

# # media = soma / len(temperaturas)
# # • A maior temperatura registrada e em qual hora ela ocorreu (índice).
# vezes = 0
# for i in range(0, len(temperaturas)):
#     if(i == 0):
#         maior = temperaturas[i]
#         indice = i
#     if(temperaturas[i] > maior):
#         maior = temperaturas[i]
#         indice = i + 1
#         vezes += 1

# print(f"\nA maior temperatura: {maior}\nHorario: {indice}\nApareceu: {vezes}º")
# print(f"A média: {media:.2f}°C")


# 3) Gestão de Poltronas em um Cinema
# Uma sala de cinema possui 120 poltronas numeradas de 0 a 119. O sistema marca True quando a poltrona está ocupada e False quando está vazia. Implemente um programa que:
# a) Crie um vetor booleano chamado poltronas = [False] * 120.
# poltronas = [False] * 120
# # b) Exiba um menu com as opções:
# # Inserir/alterar status de poltronas (use um laço de repetição e peça o número da poltrona (0-119) e o status (True/False) para atualizar os dados da poltrona até que o usuário deseje voltar ao menu principal)
# while (True):
#     op = int(input("1 - Inserir\n 2- Alterar \n 3 - Listar poltronas vazias \n 4 - Listar poltronas ocupadas \n 5 - Encerrar \n O que deseja fazer? "))

#     if(op == 1):
#         pol = int((input("Informe o numero para comprar de 0 a 119: ")))
#         if(poltronas[pol] == False):
#             poltronas[pol] = True
#             print(f"Poltrona n{pol}º comprada com sucesso!")
#         else:
#             print("Esta poltrona já esta ocupada")
#     elif(op == 2):
#         pol = int((input("Informe o numero para comprar de 0 a 119: ")))
#         if(poltronas[pol] == True):
#             poltronas[pol] = False
#             print(f"Poltrona n{pol}º alterada com sucesso")
#         else:
#             print("Esta poltrona já esta vazia")
# # Listar APENAS os números das poltronas vazias (False) e ao final a quantidade total
#     elif(op == 3):
#         PoltroDiponiveis = 0
#         print("Poltronas Disponiveis: ")
#         for i in range(0,len(poltronas)):
#             if(poltronas[i] == False):
#                 print(f"{i}")
#                 PoltroDiponiveis += 1
            
# # Listar APENAS os números das poltronas ocupadas (True) e ao final a quantidade total
#     elif(op == 4):
#         PoltroOcupadas = 0
#         print("Poltronas Ocupadas: ")
#         for i in range(0,len(poltronas)):
#             if(poltronas[i] == True):
#                 print(f"{i}")
#                 PoltroOcupadas += 1
# # Encerrar o programa.
#     elif(op == 5):
#         print("Programa finalizado!")
#         break


# 4) Análise de Vendas de um E-commerce em Dia de Promoção
# Durante uma grande promoção, um e-commerce registrou a quantidade de itens vendidos a cada minuto, por 180 minutos seguidos. O setor de Business Intelligence precisa de um relatório:
# a) Crie um vetor inteiro vendasMinuto = [0] * 180. Os valores devem ser gerados aleatoriamente pelo programa, variando de 0 a 50 vendas por minuto (inclusive).
import random
vendasMinuto = [0] * 180
for i in range(0, len(vendasMinuto)):
    vendasMinuto[i] = random.randint(0, 50)
# b) Exiba todos os valores sorteados (um por linha).
for i in range(0, len(vendasMinuto)):
    print(f"Vendas por minuto {i + 1}: {vendasMinuto[i]}")
# c) Calcule e exiba:
# O total de vendas no período total.
soma = 0
media = 0
for i in range(0, len(vendasMinuto)):
    soma += vendasMinuto[i]
print(f"\nTotal de vendas: {soma}")
# A média de vendas por minuto.
media = soma / len(vendasMinuto)
print(f"Média das vendas: {media}")
# O maior pico de vendas (maior valor do vetor) e o minuto exato em que ocorreu (índice).

for i in range(0, len(vendasMinuto)):
    if(i == 0):
        maior = vendasMinuto[i]
        indice = i
    if(vendasMinuto[i] > maior):
        maior = vendasMinuto[i]
        indice = i
print(f"\nA maior venda: {maior}\nMinuto da venda: {indice}")

# O trecho de 10 minutos consecutivos com o maior volume total de vendas (mostre o intervalo de índices e a soma correspondente).
maior_volume = 0
intervalo_inicio = 0
for i in range(0, len(vendasMinuto) - 9):  # Garantindo que o intervalo de 10 minutos não ultrapasse o limite
    total = 0
    # Soma dos valores de 10 minutos consecutivos
    for j in range(i, i + 10):
        total += vendasMinuto[j]
    # Verifica se o total da soma dos 10 minutos é maior que o maior volume registrado
    if (total > maior_volume):
        maior_volume = total
        inicio_intervalo = i

# Exibindo o intervalo e a soma
print(f"\nMaior volume total de vendas em 10 minutos: {maior_volume}")
print(f"Intervalo de índices: {intervalo_inicio + 1}")

    
