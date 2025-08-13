# Crie procedimentos com parâmetros informados pelo usuário no programa principal:
# Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve receber os números a serem somados, somar os números e apresentar o resultado na tela.
import math
def somar(a, b):
    s = a + b
    print(f"A soma é: {s}")
# Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve receber os números e realizar a operação de multiplicação, apresentando o resultado na tela.
def multiplicar(a, b):
    p = a * b
    print(f"O produto é: {p}")

# Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
def calcularRaiz(n):
    raiz = math.sqrt(n)
    print(f"A raiz é: {raiz}")
# Faça um procedimento que calcule a potência de um número (XY) chamado calcularPotencia(). O procedimento deve receber os números por parâmetro, efetuar o cálculo e apresentar o resultado.
def calcularPotencia(a, b):
    potencia = math.pow(a, b)
    print(f"A potenciação é: {potencia}")
# Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
def calcularTabuada(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i * n}")

somar(2,4)
multiplicar(3,4)
calcularRaiz(4)
calcularPotencia(2,2)
calcularTabuada(5)