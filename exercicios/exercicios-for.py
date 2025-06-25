# 01
#A) Apresente os números de 1 a 100 (um por linha).
for i in range(1, 101):
    print(i)

#B) Apresente os números de 100 a 1 (um por linha).
for i in range(100, -1 , -1):
    print(i)

#C) Apresente os números pares de 1 a 100 (um por linha).
for i in range(0, 101 , 2):
    print(i)

#D) Apresente os números ímpares de 1 a 100 (um por linha).
for i in range(1, 101, 2):
    print(i)

#E) Faça a soma dos números de 1 a 100 e ao final mostre apenas a soma total.
soma = 0
for i in range(1, 101):
    soma += i
print(soma)

#F) Faça a soma dos números de X a Y (informados pelo usuário), desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).
soma = 0
x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
for i in range(x, y + 1):
    soma += 1
print(soma)
 
#G) Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final. Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
j = int(input("Digite um valor para j: "))
fatorial = 1
for i in range(1, j + 1):
    fatorial *= i 
print(f"O fatorial de {j} é: {fatorial}")

# 02 Faça um programa que leia 5 números e informe apenas o maior número.
n = int(input("Digite o 1º número: "))
maior_numero = n
for i in range(1, 5):
    n = int(input(f"Digite o {i+1}º número: "))
    if (n > maior_numero):
        maior_numero = n
print(f"O maior número digitado é: {maior_numero}")

#03 Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for i in range(1, 6):
    n = int(input(f"Digite o {i}º número: "))
    soma += n
print(f"{soma / i}")

#04  Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for i in range(1, 51):
    if(i % 2 == 1):
        print(i)

"""
5)
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços

1 - R$ 1.99

2 - R$ 3.98

...

50 - R$ 99.50
"""
preco_unitario = 1.99
for qtd in range(1, 51):
    total = qtd * preco_unitario
print(f"{qtd} - R${total:.2f}")

#06 Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do 1 ao 10 para um número informado pelo usuário.
n = int(input("Informe um número: "))
for i in range(1, 11):
    print(f"{i} x {n} = {i * n}")

#07 Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do X a Y para um número informado pelo usuário (semelhante ao anterior, porém o usuário precisa informar três números).
n = int(input("Informe um número: "))
x= int(input("Intervalo para x: "))
y= int(input("Intervalo para y: "))
for i in range(x, y):
    print(f"{i} x {n} = {i * n}")

#08
"""
Faça um programa que gere e apresente na tela X números 
inteiros aleatórios no intervalo de -100 a 100, de modo que o valor de X seja informado pelo usuário. 
No final do programa, apresente na tela: (1) a soma dos números gerados, (2) quantos números são positivos, 
(3) negativos, (4) o maior número gerado, (5) o menor número gerado, (6) quantos são pares, (7) ímpares e (8) quantos
são múltiplos de 3.
"""
import random

qtd = int(input("Informe a quantidade a ser gerada: "))

soma = 0
maior = None
menor = None
positivo = 0
negativo = 0
pares = 0 
impares = 0
multiplo_3 = 0

print("Números gerados:\n")
for i in range(0, qtd):
    numero = random.randint(-100,100)
    soma += numero
    
    print(numero, end=" ")
    
    if(numero > 0):
        positivo += 1
    elif(numero < 0):
        negativo += 1
    
    if(numero % 2 == 0):
        pares += 1
    else:
        impares +=1
    
    if(numero % 3 == 0):
        multiplo_3  += 1
    
    if(maior is None or numero > maior):
        maior = numero
    if(menor is None or numero < menor):
        menor = numero

print("\n\nResultados:")
print(f"1. Soma dos números: {soma}")
print(f"2. Quantos são positivos: {positivo}")
print(f"3. Quantos são negativos: {negativo}")
print(f"4. Maior número gerado: {maior}")
print(f"5. Menor número gerado: {menor}")
print(f"6. Quantos são pares: {pares}")
print(f"7. Quantos são ímpares: {impares}")
print(f"8. Quantos são múltiplos de 3: {multiplo_3}")

#09
"""
Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. 
O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).

====== Menu Principal ======

1. Fazer a tabuada do 1 ao 10 para um número X

2. Apresentar os múltiplos de X entre 1 e 100

3. Apresentar a soma dos números de 1 a X

4. Sair do programa
"""
n = 0
while(n != 4):
    print("====== Menu Principal ======")
    print("1. Fazer a tabuada do 1 ao 10 para um número X")
    print("2. Apresentar os múltiplos de X entre 1 e 100")
    print("3. Apresentar a soma dos números de 1 a X")
    print("4. Sair do programa")

    opcao = int(input("Digite uma opção: "))
    if (opcao == 1):
        
        n = int(input("Informe um número para a tabuada: "))
        for i in range(1, 11):
            print(f"{i} x {n} = {i * n}")
        print()
        
    elif(opcao == 2):
        
        x = int(input("Informe um número: "))
        for i in range(1, 101):
            if (i % x == 0):
                print(i)
        print()
        
    elif(opcao == 3):
        
        soma = 0
        x = int(input("Informe um intervalo para x: "))
        for i in range(1, x + 1):
            soma += i
        print(soma)
        print()
        
    elif(opcao == 4):
        print("Escolheu consultar dados")
    else:
        print("Opção inválida. Tente novamente.")

#10
"""
Crie um jogo simples onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve adivinhar o número. 
Use um laço “while” para permitir que o usuário continue tentando até acertar. 
Após cada tentativa, informe se o palpite é maior, menor ou igual ao número sorteado.
"""
import random
numero = random.randint(1, 100)
tentativas = 0
while True:
    palpite = int(input("Chute um número entre 1 a 100: "))
    tentativas += 1
    if (palpite < 1 or palpite > 100):
        print("Apenas números entre 1 a 100")
    elif (palpite < numero):
        print("Muito baixo! Tente um número maior.\n")                    
    elif (palpite > numero):
        print("Muito alto! Tente um número menor.\n")
    else:
        print(f"Parabéns! Você acertou o número {numero} em {tentativas}º de tentativas")
        break

#11
"""
Refaça o exercício anterior, porém utilize um laço “for” para limitar o número de tentativas a 
10 (usuário tem 10 chances só para acertar).
"""
import random
numero = random.randint(1, 100)
tentativas = 0
for i in range(1, 11):
    palpite = int(input("Chute um número entre 1 a 100: "))
    tentativas += 1
    if (palpite < 1 or palpite > 100):
        print("Apenas números entre 1 a 100")
    elif (palpite < numero):
        print("Muito baixo! Tente um número maior.\n")                    
    elif (palpite > numero):
        print("Muito alto! Tente um número menor.\n")
    else:
        print(f"Parabéns! Você acertou o número {numero} em {tentativas}º de tentativas")
        break
else:
    print("Suas 10 tentativas acabaram!")

#12
"""
Crie um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes 
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo. 
No final, apresente quantos números há em cada intervalo.
"""
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

print("Digite números positivos (um por vez). Digite um número negativo para encerrar.")

while(True): 
    numero = float(input("Digite um número: "))

    if (numero < 0):
        break
    # Verifica se o número está entre 0 e 25 (inclusive)
    if (numero >= 0) and (numero <= 25):
        intervalo_0_25 += 1
    # Verifica se o número está entre 26 e 50 (inclusive)
    elif (numero >= 26) and (numero <= 50):
        intervalo_26_50 += 1
    # Verifica se o número está entre 51 e 75 (inclusive)
    elif (numero >= 51) and (numero <= 75):
        intervalo_51_75 += 1
    # Verifica se o número está entre 76 e 100 (inclusive)
    elif (numero >= 76) and (numero <= 100):
        intervalo_76_100 += 1
    else:
        print("Número fora do intervalo 0-100. Ignorado.")

print("\nResultados:")
print(f"[0-25]: {intervalo_0_25} número(s)")
print(f"[26-50]: {intervalo_26_50} número(s)")
print(f"[51-75]: {intervalo_51_75} número(s)")
print(f"[76-100]: {intervalo_76_100} número(s)")

#13
"""
Desenvolva um programa que calcule o custo total de uma viagem com base na distância a ser 
percorrida e o tipo de veículo. O custo por quilômetro varia conforme o tipo de veículo, conforme a tabela abaixo:

Tipo de Veículo
Custo por Quilômetro

Econômico
	
R$ 1,50

Médio
	
R$ 2,25

Luxo
	
R$ 3,00

O programa deve solicitar a distância a ser percorrida e o tipo de veículo. Em seguida, deve calcular 
e exibir o custo total da viagem. 
O programa deve permitir que o usuário faça novos cálculos até que ele escolha encerrar.
"""
while(True):
    distancia = float(input("\nDigite a distância da viagem (em km): "))
    if(distancia < 0):
        print("A distância não pode ser negativa.")

    # Escolha do tipo de veículo
    print("Tipos de veículo disponíveis: Econômico, Médio, Luxo")
    tipo = input("Digite o tipo de veículo: ").strip().lower()

    # Determina o custo por km com base no tipo
    if (tipo == "econômico"):
        custo_km = 1.50
    elif (tipo == "médio"):
        custo_km = 2.25
    elif (tipo == "luxo"):
        custo_km = 3.00
    else:
        print("Tipo de veículo inválido. Tente novamente.")

    # Cálculo do custo total
    custo_total = distancia * custo_km
    print(f"Custo total da viagem: R$ {custo_total:.2f}")

    # Verifica se o usuário quer fazer outro cálculo
    continuar = input("\nDeseja calcular outra viagem? (s/n): ").strip().lower()
    if(continuar != 's'):
        print("Programa encerrado.")
        break
