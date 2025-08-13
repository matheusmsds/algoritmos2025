# Crie procedimentos com parâmetros:
# Crie um procedimento que recebe um vetor de números inteiros por parâmetro. Esta função deve chamar imprimirVetor() e vai imprimir na tela todos os números do vetor informado. 
import random
def imprimirVetor(vetor):
    for i in range(0,len(vetor)):
        print(f"{vetor[i]}")
# Faça um procedimento chamado encontrarMaior() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o maior valor do vetor.
def encontrarMaior(vetor):
    for i in range(0, len(vetor)):
        if(i == 0):
            maior = vetor[i]
        if(vetor[i] > maior):
            maior = vetor[i]
    print(f"O maior valor do vetor é: {maior}")
# Faça um procedimento chamada encontrarMenor() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o menor valor do vetor.
def encontrarMenor(vetor):
    for i in range(0, len(vetor)):
        if(i == 0):
            menor = vetor[i]
        if(vetor[i] < menor):
            menor = vetor[i]

    print(f"O menor valor do vetor é: {menor}")
