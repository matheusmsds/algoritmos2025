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
