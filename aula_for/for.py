"""
n = int(input("Digite um número para a tabuada: "))
print()
for i in range(1, 11):
    print(f"{n} x {i}: {n * i}")

n = int(input("Digite um número para a tabuada: "))
x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
print()

for i in range(x, y):
    print(f"{n} x {i}: {n * i}")

EXERCIOS

EX 01
A)
for i in range(1, 101):
    print(i)
B)
for i in range(100, -1 , -1):
    print(i)
C)
for i in range(0, 101 , 2):
    print(i)
D)
for i in range(1, 101, 2):
    print(i)
E)
soma = 0
for i in range(1, 101):
    soma += i
print(soma)
F)
soma = 0
x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
for i in range(x, y + 1):
    soma += 1
print(soma)
G)
j = int(input("Digite um valor para j: "))
fatorial = 1
for i in range(1, j + 1):
    fatorial *= i 
print(f"O fatorial de {j} é: {fatorial}")

EXE 02
n = int(input("Digite o 1º número: "))
maior_numero = n
for i in range(1, 5):
    n = int(input(f"Digite o {i+1}º número: "))
    if (n > maior_numero):
        maior_numero = n
print(f"O maior número digitado é: {maior_numero}")

"""

