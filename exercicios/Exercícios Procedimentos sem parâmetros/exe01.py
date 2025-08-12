# Crie procedimentos sem parâmetros:
# Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve obter os números a serem somados, somar os números e apresentar o resultado na tela – sem parâmetros.
def somar():
    numeros = [0] * 2
    soma = 0
    for i in range(0, len(numeros)):
        numeros[i] = int(input(f"Informe o {i + 1}º número: "))
    for i in range(0, len(numeros)):
        soma += numeros[i]
    print(soma)

# Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve obter os números e realizar a operação de multiplicação, apresentando o resultado na tela – sem parâmetros.
def multiplicar():
    numeros = [0] * 2
    for i in range(0, len(numeros)):
        numeros[i] = int(input(f"Informe o {i + 1}º número: "))
    produto = numeros[0] * numeros[1]
    print(produto)

# Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz(). O procedimento deve pedir o número ao usuário, efetuar o cálculo e apresentar o resultado – sem parâmetros.
import math
def calcularRaiz():
    n = int(input("Informe um número: "))
    raiz = math.sqrt(n)
    print(f"Raiz quadrada: {raiz:.2f}")

# Faça um procedimento que calcule a potência de um número (XY) chamado calcularPotencia(). O procedimento deve pedir os números ao usuário, efetuar o cálculo e apresentar o resultado – sem parâmetros.
def calcularPotencia():
    numeros = [0] * 2
    for i in range(0, len(numeros)):
        numeros[i] = int(input(f"Informe o {i + 1}º número: "))
    potencia = math.pow(numeros[0], numeros[1])
    print(f"Potencia: {potencia}")

# Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada(). O procedimento deve pedir o número ao usuário, efetuar os cálculos e apresentar os resultados – sem parâmetros.
def calcularTabuada():
    n = int(input("Informe um número: "))
    for i in range(1, 11):
        print(f"{i} x {n} = {i * n}")