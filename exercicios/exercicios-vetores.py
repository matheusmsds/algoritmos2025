# # 1)
# Para cada conjunto de valores abaixo, escreva o código necessário para criar vetores:
# a) 9  18  41  65  88  121
a = [9, 18, 41, 65, 88, 121]
# b) Rafael   Ayslan   Daniela   Frank
b = ["Rafale", "Asylan", "Daniela", "Frank"]
# c) 3290,90   128,50   85,90   789,31
c = [3290.90, 128.50, 85.90, 789,31]
#d) Um vetor com tamanho 5 e preenchido com números fornecidos também pelo usuário.
vetor = [0] * 5

vetor[0] = int(input())
vetor[1] = int(input())
vetor[2] = int(input())
vetor[3] = int(input())
vetor[4] = int(input())

# 2)
# Considerando o vetor criado no exercício 1.d:
vetor = [0] * 5


print("Digite 5 números inteiros:")

vetor[0] = int(input("Digite o 1º número: "))
vetor[1] = int(input("Digite o 2º número: "))
vetor[2] = int(input("Digite o 3º número: "))
vetor[3] = int(input("Digite o 4º número: "))
vetor[4] = int(input("Digite o 5º número: "))


# a) Apresente na tela todos os valores do vetor.
print("\n--- a) Valores na ordem original ---")
print(vetor[0])
print(vetor[1])
print(vetor[2]) 
print(vetor[3])
print(vetor[4])


# b) Apresente na tela todos os valores do vetor em ordem invertida (de trás para frente).
print("\n--- b) Valores em ordem invertida ---")
print(vetor[4])
print(vetor[3])
print(vetor[2]) 
print(vetor[1])
print(vetor[0])


# c) Apresente na tela o dobro de todos os valores do vetor.
print("\n--- c) Dobro de cada valor ---")
print(vetor[0] * 2)
print(vetor[1] * 2)
print(vetor[2] * 2) 
print(vetor[3] * 2)
print(vetor[4] * 2)

# d) Apresente na tela a metade de todos os valores do vetor.
print("\n--- d) Metade de cada valor ---")
print(vetor[0] / 2)
print(vetor[1] / 2)
print(vetor[2] / 2) 
print(vetor[3] / 2)
print(vetor[4] / 2)


#3
"""
Crie um vetor de strings para armazenar quatro dados do usuário: nome completo, endereço, telefone e email.
Apresente na tela, de maneira organizada, todos os dados do usuário, exemplo:
Nome completo: 	Rafael Zottesso
Endereço: 		Rua ABC, 123
Telefone: 		(99) 99999-9999
E-mail: 			rafael.zottesso@ifpr.edu.br
Obs.: para dar esse “espaço” utilize o código da tabulação \t. Cada linha precisa de uma quantidade diferente de tabulação. Você pode colocar várias usando \t\t\t, por exemplo.

"""

vetor_str = [""] * 4
vetor_str[0] = input("Nome completo: ")
vetor_str[1] = input("Endereço: ")
vetor_str[2] = input("Telefone: ")
vetor_str[3] = input("E-mail: ")



print(f"Nome completo:\t{vetor_str[0]}\nEndereço:\t{vetor_str[1]}\nTelefone:\t{vetor_str[2]}\nEmail:\t{vetor_str[3]}")

# 4) Crie um vetor com 4 números decimais (ponto-flutuante) de modo que o usuário do programa vá digitar esses valores.
vetor_float = [0.0] * 4

vetor_float[0] = float(input("Digite um número ponto flutuante: "))
vetor_float[1] = float(input("Digite um número ponto flutuante: "))
vetor_float[2] = float(input("Digite um número ponto flutuante: "))
vetor_float[3] = float(input("Digite um número ponto flutuante: "))

# a) Apresente na tela a soma de todos os valores.
soma = (vetor_float[0] + vetor_float[1] + vetor_float[2] + vetor_float[3])
print(f"\na) A soma dos valores é: {soma}")

# b) Apresente na tela a média de todos os valores.
media = (soma / 4)
print(f"b) A média entre os valores é: {media}")

# c) Apresente na tela o produto (multiplicação) de todos os valores.
produto = (vetor_float[0] * vetor_float[1] * vetor_float[2] * vetor_float[3])
print(f"c) O produto dos valores é: {produto}")

# d) Apresente na tela somente quantos valores são maiores do que 1000.
maior_1000 = 0
if (vetor_float[0] > 1000):
    maior_1000 += 1
if (vetor_float[1] > 1000):
    maior_1000 += 1
if (vetor_float[2] > 1000):
    maior_1000 += 1
if (vetor_float[3] > 1000):
    maior_1000 += 1
print(f"d) Quantidade de valores maiores que 1000: {maior_1000}")

# e) Apresente na tela a quantidade de valores que são maiores do que zero.
maior_que_zero = 0
if (vetor_float[0] > 0):
    maior_que_zero += 1
if (vetor_float[1] > 0):
    maior_que_zero += 1
if (vetor_float[2] > 0):
    maior_que_zero += 1
if (vetor_float[3] > 0):
    maior_que_zero += 1
print(f"e) Quantidade de valores maiores que zero: {maior_que_zero}")

# f) Apresente na tela quantos valores são pares (números inteiros divisíveis por 2).
pares = 0
if ((vetor_float[0] % 2 == 0) and (vetor_float[0] == int(vetor_float[0]))):
    pares += 1
if ((vetor_float[1] % 2 == 0) and (vetor_float[1] == int(vetor_float[1]))):
    pares += 1
if ((vetor_float[2] % 2 == 0) and (vetor_float[2] == int(vetor_float[2]))):
    pares += 1
if ((vetor_float[3] % 2 == 0) and (vetor_float[3] == int(vetor_float[3]))):
    pares += 1
print(f"f) Quantidade de valores pares: {pares}")

# g) Apresente na tela somente o maior valor do vetor.
maior_valor = vetor_float[0]
if (vetor_float[1] > maior_valor):
    maior_valor = vetor_float[1]
if (vetor_float[2] > maior_valor):
    maior_valor = vetor_float[2]
if (vetor_float[3] > maior_valor):
    maior_valor = vetor_float[3]
print(f"g) O maior valor é: {maior_valor}")

# h) Apresenta na tela somente o índice do maior valor do vetor.
indice_maior = 0
maior_valor = vetor_float[0]
if (vetor_float[1] > maior_valor):
    maior_valor = vetor_float[1]
    indice_maior = 1
if (vetor_float[2] > maior_valor):
    maior_valor = vetor_float[2]
    indice_maior = 2
if (vetor_float[3] > maior_valor):
    maior_valor = vetor_float[3]
    indice_maior = 3
print(f"h) O índice do maior valor é: {indice_maior}")

# i) Apresente na tela somente o menor valor do vetor.
menor_valor = vetor_float[0]
if (vetor_float[1] < menor_valor):
    menor_valor = vetor_float[1]
if (vetor_float[2] < menor_valor):
    menor_valor = vetor_float[2]
if (vetor_float[3] < menor_valor):
    menor_valor = vetor_float[3]
print(f"i) O menor valor é: {menor_valor}")

# j) Apresenta na tela somente o índice do menor valor do vetor.
indice_menor = 0
menor_valor = vetor_float[0]
if (vetor_float[1] < menor_valor):
    menor_valor = vetor_float[1]
    indice_menor = 1
if (vetor_float[2] < menor_valor):
    menor_valor = vetor_float[2]
    indice_menor = 2
if (vetor_float[3] < menor_valor):
    menor_valor = vetor_float[3]
    indice_menor = 3
print(f"j) O índice do menor valor é: {indice_menor}")


#5
""" 
Você foi contratado para criar um programa para uma loteria.
A loteria tem apenas um tipo de jogo que sorteia 06 números inteiros e eles podem ser repetidos.
Porém o intervalo de números para o sorteio é de 1 a 15. Por exemplo:
Sorteio A: 9 - 2 - 14 - 9 - 5 - 12
Sorteio B: 12 - 12 - 1 - 13 - 7 - 8 - 9
Crie um programa para a loteria sortear seis números inteiros e armazenar em um vetor. 
"""
import random

n = random.randint(1,15)
numeros_sorteados = [0] * 6
numeros_sorteados = [random.randint(1,15), random.randint(1,15),random.randint(1,15),random.randint(1,15),random.randint(1,15),random.randint(1,15)]


print(f"Sorteio A: {numeros_sorteados[0]} - {numeros_sorteados[1]} - {numeros_sorteados[1]} - {numeros_sorteados[2]} - {numeros_sorteados[3]} - {numeros_sorteados[4]} - {numeros_sorteados[5]}")

""" 
A loteria expandiu seus jogos e agora criou uma nova modalidade, 
que sorteia 05 números de 1 a 4 e o jogador deve acertar quantas vezes um determinado número foi repetido. Por exemplo:
Sorteio A: 1 - 4 - 2 - 1 - 3

Ocorrências:
1 - 2 vezes
2 - 1 vez
3 - 1 vez
4 - 1 vez

O jogador deve informar duas coisas: primeiro um número entre 1 e 4 e depois quantas vezes esse número foi repetido. Por exemplo:

Jogador 1					Jogador 2
Número escolhido: 2			Número escolhido: 1
Repetições: 2				Repetições: 2
Resultado: Jogador perdeu		Resultado: Jogador venceu

Faça um programa que sorteie 5 números entre 1 e 4 e armazene em um vetor. 
Em seguida, pergunte ao usuário o número escolhido e a quantidade de repetições do número escolhido. 
Por fim, informe na tela os números sorteados e se o jogador venceu ou perdeu.
 """
import random

sorteio = [0] * 5
sorteio = [random.randint(1,4), random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)]

numero_escolhido = int(input("Digite um número entre 1 a 4: "))
rep_informadas = int(input("Quantas vezes esse número foi repetido: "))

status = ""
contador = 0

if(sorteio[0] == numero_escolhido):
    contador += 1
if(sorteio[1] == numero_escolhido):
    contador += 1
if(sorteio[2] == numero_escolhido):
    contador += 1
if(sorteio[3] == numero_escolhido):
    contador += 1
if(sorteio[4] == numero_escolhido):
    contador += 1

print(f"Sorteio A: {sorteio[0]} - {sorteio[1]} - {sorteio[2]} - {sorteio[3]} - {sorteio[4]}")

if(contador == rep_informadas):
    status = "Jogador Venceu"
else:
    status = "Jogador Perdeu"

print(f"Número escolhido: {numero_escolhido}\nRepetições: {contador}\nResultado: {status}")
