# numeros = [0] * 100
# 01
#A) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
# for i in range(0, len(numeros)):
#     numeros[i] = i + 1
#     print(f"Número: {numeros[i]}")

#B) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
# for i in range(len(numeros) -1, -1, -1):
#     numeros[i] = i + 1
#     print(f"Número: {numeros[i]}")

#C) Mostre na tela o dobro de todos os números.
# for i in range(0, len(numeros)):
#     numeros[i] = i + 1
#     print(f"Dobro: {numeros[i] * 2}")

#D) Apresente na tela a soma de todos os números.
# soma = 0
# for i in range(0, len(numeros)):
#     numeros[i] = i + 1
#     soma += numeros[i]
# print(f"Soma: {soma}")

#E) Apresente na tela a média geral dos valores contidos na lista.
# soma = 0
# for i in range(0, len(numeros)):
#     numeros[i] = i + 1
#     soma += numeros[i]
# print(f"Soma: {soma/ len(numeros):.2f}")

#F) Mostre na tela a quantidade de números pares.
# x = 0
# for i in range(0, len(numeros)):
#     numeros[i] = x
#     x += 2
#     print(f"Número: {numeros[i]}")


#2)
#Faça um programa para armazenar 6 números inteiros para uma loteria, 
#permitindo que o usuário informe os números. Depois de preencher, informe uma mensagem e os
#números sorteados.
# import random
# n = [0] * 6

# for i in range(0, len(n)):
#     n[i] = int(input(f"Informe o {i + 1}º: "))

# print("Números Sorteados: ")
# for i in range(0, len(n)):
#     print(f"{random.choice(n)}")

#3)
# Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso. 
# Faça um programa para armazenar 5 nomes e permitir que o professor digite o nome de cada um. 
# Em seguida, apresente na tela todos os nomes informados.
# nomes = [""] * 5
# for i in range(0, len(nomes)):
#     nomes[i] = input(f"Informe o {i + 1}º: ")
# print()
# for i in range(0, len(nomes)):
#     print(f"{i + 1}º nome: {nomes[i]}")

#4)
# Faça um programa que peça para o usuário informar o tamanho de um vetor. 
# Em seguida, crie este vetor e preencha ele com números digitados pelo usuário. 
# Por fim, apresente na tela os números digitados.
# tamanho = int(input("Informe o tamanho do vetor: "))
# numeros = [0] * tamanho

# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# for i in range(0, len(numeros)):
#     print(f"{numeros[i]}")

#5) Para os exercícios abaixo, utilize o vetor criado no exercício anterior.
#tamanho = int(input("Informe o tamanho do vetor: "))
#numeros = [0] * tamanho

#A) Apresente os números do vetor em ordem inversa.
# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# for i in range(len(numeros) -1, -1, -1):
#     print(f"{numeros[i]}")

#B) Apresente a soma de todos os elementos.
# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# soma = 0
# for i in range(0, len(numeros)):
#     soma += numeros[i]
# print(f"Soma: {soma}")

#C) Calcule a média aritmética dos valores.
# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# soma = 0
# for i in range(0, len(numeros)):
#     soma += numeros[i]
# print(f"Média: {soma/len(numeros)}")

#D) Liste na tela somente os números do vetor que estão em posições (índices) pares.
# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# for i in range(0, len(numeros)):
#     if(numeros[i] % 2 == 0):
#         print(f"{numeros[i]}")

#E)
# Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar os números na tela. 
#Por exemplo: 
# Na sequência [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1] o usuário teria que informar 4 (na posição inicial) e 8 
#(posição final) para mostrar na tela somente:  3, 14, 10, -3, 9.

# numeros = [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
# pos_inicial = int(input("Informe um indice inicial: "))
# pos_final = int(input("Informe um indice final: "))

# for i in range(pos_inicial, pos_final + 1):
#     print(numeros[i])

#F)
# Semelhante ao anterior, porém deve-se fazer a soma dos valores contidos no vetor conforme a posição e inicial informada. Exemplo: 
# Na sequência [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1] , o usuário teria que informar 4 (na posição inicial) e 8 (posição final) 
#para realizar a soma do segmento destacado 
# numeros = [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
# pos_inicial = int(input("Informe um indice inicial: "))
# pos_final = int(input("Informe um indice final: "))

# soma = 0
# for i in range(pos_inicial, pos_final + 1):
#     soma += numeros[i]
# print(soma)

#G) Encontre qual é o maior e o menor número desta lista.
# tamanho = int(input("Informe o tamanho do vetor: "))
# numeros = [0] * tamanho

# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))

# for i in range(0, len(numeros)):
#     if(i == 0):
#         maior = numeros[i]
#         menor = numeros[i]

#     if(numeros[i] > maior):
#         maior = numeros[i]
#     if(numeros[i] < menor):
#         menor = numeros[i]

# print(f"\nMaior indice: {maior}\nMenor indice: {menor}")

#H) Encontre qual é o maior e o menor número desta lista. Além disso, informe quais são os índices (posições) deles.
# tamanho = int(input("Informe o tamanho do vetor: "))
# numeros = [0] * tamanho

# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))

# for i in range(0, len(numeros)):
#     if(i == 0):
#         maior = numeros[i]
#         menor = numeros[i]
#         indice_maior = i
#         indice_menor = i
        
#     if(numeros[i] > maior):
#         maior = numeros[i]
#         indice_maior = i
#     if(numeros[i] < menor):
#         menor = numeros[i]
#         indice_menor = i

# print(f"\nMaior numero: {maior} indice {indice_maior}\nMenor indice: {menor} indice {indice_menor}")

#I) Informe quantos números pares e ímpares foram digitados (apenas a quantidade de cada).
# tamanho = int(input("Informe o tamanho do vetor: "))
# numeros = [0] * tamanho

# pares = 0
# impares = 0

# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# for i in range(0, len(numeros)):
#     if(numeros[i] % 2 == 0):
#         pares += 1
#     if(numeros[i] % 2 == 1):
#         impares += 1
# print(f"pares: {pares}\nimpares: {impares}")

#6) Crie um vetor para armazenar alguns números que serão utilizados no cálculo da tabuada.
# tamanho = int(input("Informe o tamanho do vetor: "))
# numeros = [0] * tamanho

# A) Apresente todos os números informados e seu respectivo dobro.
# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# print("Números: ")
# for i in range(0, len(numeros)):
#     print(f"{numeros[i]}")
# print("Dobro deles: ")
# for i in range(0, len(numeros)):
#     print(f"{numeros[i] * 2}")

#B) Para cada número presente no vetor, faça a tabuada do 1 ao 10 para ele (utilizando laço de repetição você vai 
#criar uma tabuada para cada valor do vetor).
# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Informe o {i + 1}º: "))
# for i in range(0, len(numeros)):
#     numero = numeros[i]
#     for j in range(1, 11):
#         print(f"{numero} x {j} = {numero * j}")

# 7) Maria está organizando um chá de bebê e precisa fazer a lista de convidados. Ela gostaria de saber quantas pessoas irão comparecer ao evento.
# Crie um algoritmo que solicite ao usuário que digite o número de convidados e, em seguida, armazene a quantidade em uma variável. 
# Utilize um laço de repetição para pedir o nome de cada convidado e armazená-lo em um vetor. Ao final, exiba a quantidade de convidados.

# qtd_pessoas = int(input("Informe a quantidade de pessoas: "))
# convidados = [""] * qtd_pessoas

# for i in range(0, len(convidados)):
#     convidados[i] = input("Nome: ")
# print("Convidados: \n")
# for i in range(0, len(convidados)):
#     print(f"{convidados[i]}")
# print(f"\nQuantidade de convidados: {qtd_pessoas}")

# 8) Roberto é um vendedor que precisa calcular sua comissão mensal. Ele recebe uma porcentagem de cada venda realizada. 
# Crie um algoritmo que solicite ao vendedor o número de vendas efetuadas no mês e armazene-o em uma variável. 
# Utilize um laço de repetição para solicitar o valor de cada venda e armazená-lo em um vetor.
# Em seguida, calcule a comissão total do vendedor, sabendo que a comissão é:

#5% para vendas até R$999,99
#4% para vendas entre R$1.000 e R$1.999
#3% para vendas acima de R$2.000

# quantidade_vendas = int(input("Digite o número de vendas efetuadas no mês: "))
# valores_vendas = [0.0] * quantidade_vendas
# comissao_total = 0

# for i in range(0, quantidade_vendas):
#     valores_vendas[i] = float(input(f"Digite o valor da venda {i + 1}: R$ "))

# for i in range(0 ,quantidade_vendas):
#     valor = valores_vendas[i]
#     if (valor <= 999.99):
#         comissao = valor * 0.05
#     elif (valor >= 1000 and valor <= 1999.99):
#         comissao = valor * 0.04
#     else:
#         comissao = valor * 0.03

#     comissao_total += comissao

# print(f"\nComissão total do mês: R$ {comissao_total:.2f}")

#9) Um professor precisa armazenar uma lista de n alunos e seus respectivos conceitos. Crie um programa para auxiliar este professor.

# qtd = int(input("Informe a quantidade de alunos: "))
# nomes = [""] * qtd
# conceitos = [""] * qtd

# for i in range(0, qtd):
#     nomes[i] = input(f"Informe o nome do {i + 1}º aluno: ")
#     while (True):
#         c = input(f"Conceito do aluno {nomes[i]} (D, C, B, A): ").upper()
#         conceitos[i] = c
#         break
# print("\nLista de alunos e conceitos: ")
# for j in range(0, qtd):
#     print(f"{nomes[j]} - {conceitos[j]}")

#10) Faça um programa para armazenar seis números inteiros para uma loteria, permitindo que o usuário informe os números sorteados. 
# Em seguida, peça para o usuário informar os seis números que ele apostou. Por fim, apresente na tela quantos números ele acertou, 
# informando se ele não ganhou nada (0 a 3 acertos), se acertou a quadra (4 acertos), a quina (5 acertos) ou se ele nunca mais vai precisar trabalhar (6 acertos).
# numeros_sorteados = [0] * 6
# numeros = [0] * 6

# acertos = 0

# for i in range(0, len(numeros_sorteados)):
#     numeros_sorteados[i] = int(input("Informe os números sorteados: "))
# for j in range(0,len(numeros_sorteados)):
#     numeros[j] = int(input("Informe os números apostados: "))
#     if(numeros[j] == numeros_sorteados[j]):
#         acertos += 1

# print(f"\nVocê acertou {acertos} número(s).")

# if (acertos <= 3):
#     print("Você não ganhou nada.")
# elif (acertos == 4):
#     print("Parabéns! Você acertou a quadra!")
# elif (acertos == 5):
#     print("Parabéns! Você acertou a quina!")
# elif (acertos == 6):
#     print("Parabéns! Você nunca mais vai precisar trabalhar!")

#11)Faça um programa para armazenar seis números inteiros para uma loteria, de modo que os seis números sejam criados aleatoriamente pelo Python e que não sejam repetidos. 
#Em seguida, peça para o usuário informar os seis números que ele apostou.
#Por fim, apresente na tela quantos números ele acertou, informando se ele não ganhou nada (0 a 3 acertos), se acertou a quadra (4 acertos), a 
#quina (5 acertos) ou se ele nunca mais vai precisar trabalhar (6 acertos).
# import random
# numeros_sorteados = random.sample(range(1, 61), 6)
# numeros = [0] * 6

# acertos = 0

# for j in range(0,len(numeros_sorteados)):
#     numeros[j] = int(input("Informe os números apostados: "))
#     if(numeros[j] == numeros_sorteados[j]):
#         acertos += 1

# print(f"\nVocê acertou {acertos} número(s).")

# if (acertos <= 3):
#     print("Você não ganhou nada.")
# elif (acertos == 4):
#     print("Parabéns! Você acertou a quadra!")
# elif (acertos == 5):
#     print("Parabéns! Você acertou a quina!")
# elif (acertos == 6):
#     print("Parabéns! Você nunca mais vai precisar trabalhar!")

#12) Considerando que uma palavra (string) pode ser percorrida como um vetor, faça um programa que peça o nome de uma pessoa e o apresente de trás para frente.
# nome = input("Informe seu nome: ")
# nome_invertido = ""
# for i in range(len(nome) - 1, -1 , -1):
#     nome_invertido += nome[i]
# print(nome_invertido)

#13) Um esquema de sorteio precisa armazenar uma lista de 10 pessoas e ao final sortear uma delas aleatoriamente. Faça um programa para este esquema.
# import random
# pessoas = [""] * 10
# for i in range(0, len(pessoas)):
#     pessoas[i] = input(f"Informe o nome da {i + 1}º: ")

# print(f"A pessoa sorteada foi: {random.choice(pessoas)}")

#14) Um esquema de sorteio precisa armazenar um banco de 10 palavras informadas pelo usuário e ao final sortear uma delas aleatoriamente. 
#Em seguida, o programa deve perguntar para o usuário uma letra e verificar quantas vezes essa letra aparece na palavra sorteada.
# import random
# palavras = [""] * 10

# for i in range(0, len(palavras)):
#     palavras[i] = input(f"Informe a {i + 1}º palavra: ")

# palavra = random.choice(palavras)

# letra = input("Informe uma letra: ")
# vezes = 0
# for i in range(0, len(palavra)):
#     if(letra == palavra[i]):
#         vezes += 1

# print(f"A letra {letra} aparece {vezes}º de vezes")

#15)
# Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
#positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# perguntas = [
#     "Telefonou para a vítima?",
#     "Esteve no local do crime?",
#     "Mora perto da vítima?",
#     "Devia para a vítima?",
#     "Já trabalhou com a vítima?"
# ]

# respostas = [""] * 5
# positivas = 0

# for i in range(0, len(respostas)):
#     resposta = input(f"{perguntas[i]} (s/n): ").strip().lower()
#     if(resposta == 's'):
#         positivas += 1
#     respostas[i] = resposta

# print(f"\nTotal de respostas positivas: {positivas}")

# if (positivas == 2):
#     print("Classificação: Suspeita")
# elif (positivas == 3 or positivas == 4):
#     print("Classificação: Cúmplice")
# elif (positivas == 5):
#     print("Classificação: Assassino")
# else:
#     print("Classificação: Inocente")


#16) Fulano de Tal está organizando um campeonato de futebol para n times. 
#Ele precisa armazenar o nome do time e a pontuação final de cada time. Ao final, precisa saber qual foi o time campeão e o vice campeão. 
#Faça um programa para o Fulano de Tal.
# Número de times
# n = int(input("Quantos times participarão do campeonato? "))

# # Inicializa listas
# nomes = [""] * n
# pontos = [0] * n

# # Entrada dos dados
# for i in range(n):
#     nomes[i] = input(f"Nome do {i + 1}º time: ")
#     pontos[i] = int(input(f"Pontuação do time {nomes[i]}: "))

# # Inicializa variáveis para campeão e vice
# campeao_idx = 0
# vice_idx = -1

# for i in range(1, n):
#     if (pontos[i] > pontos[campeao_idx]):
#         vice_idx = campeao_idx
#         campeao_idx = i
#     elif (vice_idx == -1 or pontos[i] > pontos[vice_idx] and i != campeao_idx):
#         vice_idx = i

# print(f"\nCampeão: {nomes[campeao_idx]} com {pontos[campeao_idx]} pontos")
# print(f"Vice-campeão: {nomes[vice_idx]} com {pontos[vice_idx]} pontos")
