# Exercício 02: Um programa de computador deve ser capaz de armazenar dados sobre as partes de uma casa.
# Como a casa possui vários cômodos e cada cômodo possui uma porta, precisa-se de uma estrutura capaz de
# representar as portas da casa. Sabe-se que toda porta deve ter registrado a sua largura, sua altura, seu peso e
# o seu material (ex: madeira, alumínio, etc.). Crie três objetos que representem portas (ex: porta da sala, porta

class Porta:
    def __init__(self):
        self.altura = 0.0
        self.material = ""
        self.peso = 0.0
        self.comodo = ""

def obterPorta():
    porta = Porta()
    porta.altura = float(input("Informe a altura da porta: "))
    porta.material = input("Informe o tipo de material da porta: ")
    porta.peso = float(input("Informe o peso da porta: "))
    porta.comodo = input("Informe o cômodo da porta: ")
    print()
    return porta

def mostrarPorta(porta):
    print()
    print(f"Altura: {porta.altura}\nMaterial: {porta.material}\nPeso: {porta.altura}\nCômodo: {porta.comodo}\n")

qtd = int(input("Informe a quantidade de portas que deseja registrar: "))
listaPortas = [Porta()] * qtd

for cont in range(0, len(listaPortas)):
    print(f"{cont + 1}º Porta")
    listaPortas[cont] = obterPorta()

for cont in range(0, len(listaPortas)):
    print(f"{cont + 1}º Porta")
    mostrarPorta(listaPortas[cont])
