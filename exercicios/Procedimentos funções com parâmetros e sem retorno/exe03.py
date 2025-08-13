import random
from exe02 import *

numeros = [0] * 10
for i in range(0, len(numeros)):
    numeros[i] = random.randint(1, 100)

imprimirVetor(numeros)
encontrarMaior(numeros)
encontrarMenor(numeros)