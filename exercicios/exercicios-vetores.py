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
# a) Apresente na tela todos os valores do vetor.
print(vetor[0])
print(vetor[1])
print(vetor[2]) 
print(vetor[3])
print(vetor[4])
# b) Apresente na tela todos os valores do vetor em ordem invertida (de trás para frente).
print(vetor[4])
print(vetor[3])
print(vetor[2]) 
print(vetor[1])
print(vetor[0])
# c) Apresente na tela o dobro de todos os valores do vetor.
print(vetor[4] * 2)
print(vetor[3] * 2)
print(vetor[2] * 2) 
print(vetor[1] * 2)
print(vetor[0] * 2)
# d) Apresente na tela a metade de todos os valores do vetor.
print(vetor[4] / 2)
print(vetor[3] / 2)
print(vetor[2] / 2) 
print(vetor[1] / 2)
print(vetor[0] / 2)

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

vetor_float = [0.0] * 4
# Crie um vetor com 4 números decimais (ponto-flutuante) de modo que o usuário do programa vá digitar esses valores.
vetor_float[0] = float(input("Digite um número ponto flutuante: "))
vetor_float[1] = float(input("Digite um número ponto flutuante: "))
vetor_float[2] = float(input("Digite um número ponto flutuante: "))
vetor_float[3] = float(input("Digite um número ponto flutuante: "))
# a) Apresente na tela a soma de todos os valores.
soma = vetor_float[0] + vetor_float[1] + vetor_float[2] + vetor_float[3]
print(f"A soma dos valores é: {soma}")
# b) Apresente na tela a média de todos os valores.
soma = vetor_float[0] + vetor_float[1] + vetor_float[2] + vetor_float[3]
print(f"A média entre os valores é: {soma / 5}")
# c) Apresente na tela o produto (multiplicação) de todos os valores.
produto = vetor_float[0] * vetor_float[1] * vetor_float[2] * vetor_float[3]
print(f"O produdo dos valores é: {produto}")
# d) Apresente na tela somente quantos valores são maiores do que 1000.
if(vetor_float[0] > 1000):
    print(vetor_float[0])
elif(vetor_float[1] > 1000):
    print(vetor_float[1])    
elif(vetor_float[2] > 1000):
    print(vetor_float[2])    
elif(vetor_float[3] > 1000):
    print(vetor_float[3])
# # e) Apresente na tela a quantidade de valores que são maiores do que zero.
if(vetor_float[0] > 0):
    print(vetor_float[0])
elif(vetor_float[1] > 0):
    print(vetor_float[1])    
elif(vetor_float[2] > 0):
    print(vetor_float[2])    
elif(vetor_float[3] > 0):
    print(vetor_float[3])
# # f) Apresente na tela quantos valores são pares.

if(vetor_float[0] % 2 == 0):
    print(vetor_float[0])
elif(vetor_float[1] % 2 == 0):
    print(vetor_float[1])    
elif(vetor_float[2] % 2 == 0):
    print(vetor_float[2])    
elif(vetor_float[3] % 2 == 0):
    print(vetor_float[3])

# # g) Apresente na tela somente o maior valor do vetor.
maior_valor = vetor_float[0]
if(vetor_float[1] > maior_valor):
   maior_valor = vetor_float[1]
elif(vetor_float[2] > maior_valor):
    maior_valor = vetor_float[2]    
elif(vetor_float[3] > maior_valor):
    maior_valor = vetor_float[3] 

# print(f"O maior valor é {maior_valor}")

# h) Apresenta na tela somente o índice do maior valor do vetor.
indice_maior = 0
maior_valor = vetor_float[0]
if(vetor_float[1] > maior_valor):
   maior_valor = vetor_float[1]
   indice_maior = 1
elif(vetor_float[2] > maior_valor):
    maior_valor = vetor_float[2]
    indice_maior = 1

elif(vetor_float[3] > maior_valor):
    maior_valor = vetor_float[3]
    indice_maior = 1

print(f"O indice do maior valor é {indice_maiorr}")

# i) Apresente na tela somente o menor valor do vetor.

menor_valor  = vetor_float[0]
if(vetor_float[1] > menor_valor):
   menor_valor = vetor_float[1]
elif(vetor_float[2] > menor_valor):
    menor_valor = vetor_float[2]
elif(vetor_float[3] > maior_valor):
    maior_valor = vetor_float[3]
print(f"O menor valor é {menor_valor}")
# j) Apresenta na tela somente o índice do menor valor do vetor.
menor_valor = vetor_float[0]
if(vetor_float[1] < maior_valor):
   menor_valor = vetor_float[1]
elif(vetor_float[2] < maior_valor):
    menor_valor = vetor_float[2]    
elif(vetor_float[3] < maior_valor):
    menor_valor = vetor_float[3]
print(f"O menor valor é {maior_valor}")
