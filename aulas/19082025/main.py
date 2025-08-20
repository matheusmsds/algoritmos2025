from funcs import * 

# while(True):
#     n = inputInt("Informe um número: ")
    
#     if(ePrimo(n)):
#         print(f"O número {n} é um número primo")
#     else:
#         print(f"O número {n} não é um número primo")


count = 0
soma = 0
for i in range(2, 101):
    if(ePrimo(i)):
        count += 1
        soma += i
        print(i, end=" ")

# print(f"\nTotal de números primos: {count}")
# print(f"A soma de todos os números primos: {soma}")

qtd = int(input("Quantos números vão ser verificados: "))

numeros = [0] * qtd
for i in range(0, len(numeros)):
    numeros[i] = inputInt(f"Informe o {i + 1}º número: ")

print("São números primos: ")
for i in range(0, len(numeros)):
    if(ePrimo(numeros[i])):
        print(f"{numeros[i]}")

print("")