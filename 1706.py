import random



print("---------Gerador de números 2000---------")
max = int(input("Informe um valor x: "))
min = int(input("Informe um valor y: "))

qtd = int(input("Informe a quantidade a ser gerada: "))

print("------------------")

if (max > min):
    temp = max
    max = min
    min = temp

soma = 0
maior = max
menor = min

for i in range(0, qtd):
    numero = random.randint(max,min)
    soma += numero
    
    if(numero > maior):
        maior = numero
    if(numero < menor):
        menor = numero
    
    print(numero)

print(f"\n------------------Relátorio------------------\nmaior número:{maior}\nmenor número:{menor}\nsoma dos números sorteados: {soma}\n------------------------------------")
