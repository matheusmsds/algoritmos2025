from exe01 import *

# Faça um programa que apresente um menu para o usuário com opções para cada procedimento criado no exercício
# 1: soma, multiplicação, raiz, potência e tabuada, além de uma opção para sair do programa. 
# Ao escolher uma opção, execute o procedimento adequado.

while(True):
    print(" --- Menu ---")
    print("1 - Soma")
    print("2 - Multiplicação")
    print("3 - Raiz")
    print("4 - Potência")
    print("5 - Tabuada")
    print("0 - Sair")
    n = int(input("Escolha uma opção: "))

    if(n == 1):
        somar()
    elif(n == 2):
        multiplicar()
    elif(n == 3):
        calcularRaiz()
    elif(n == 4):
        calcularPotencia()
    elif(n == 5):
        calcularTabuada()
    elif(n == 0):
        break