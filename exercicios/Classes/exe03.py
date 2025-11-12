# Exercício 03: Escreva um modelo para representar uma lâmpada que está à venda em um supermercado. Que
# atributos devem ser representados por este modelo?

from itertools import count
from operator import le


class Lampada:
    def __init__(self):
        self.tipo = ""
        self.cor_temperatura =  ""
        self.voltagem = ""
        self.preco = 0.0

def obterLampada():
    lampada = Lampada()
    lampada.tipo = input("Tipo da lampada: ")
    lampada.cor_temperatura = input("Cor da lampada: ")
    lampada.voltagem = input("Voltagem(Ex: Bivolt):")
    lampada.preco = float(input("Preço da lampada: "))
    print()
    return lampada

def mostrarLampada(lampada):
    print(f"Tipo: {lampada.tipo}\nCor: {lampada.cor_temperatura}\nVoltagem: {lampada.voltagem}\nPreço: R${lampada.preco:.2f}\n")

qtd = int(input("Quantidade de lampadas: "))
lista_lampadas = [Lampada()] * qtd

for cont in range(0, len(lista_lampadas)):
    print(f"{cont + 1}º Lampada")
    lista_lampadas[cont] = obterLampada()

for cont in range(0, len(lista_lampadas)):
    print(f"{cont + 1}º Lampada")
    mostrarLampada(lista_lampadas[cont])