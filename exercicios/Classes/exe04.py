# Exercício 04: Considere que uma lâmpada possua os seguintes estados: apagada e acesa. Implemente uma
# estrutura capaz de representar o estado da lâmpada.
# Implemente um método (função ou procedimento) chamado ascenderLuz que receba a lâmpada por
# parâmetro e faça com que a lâmpada fique acesa. Implemente o método pagarLuz que receba a lâmpada por
# parâmetro e faça com que a lâmpada fique apagada. Implemente o método exibirLuz que receba a lâmpada
# como parâmetro e apresente uma mensagem informando se a lâmpada está acesa ou apagada.

class Lampada:
    def __init__(self):
        self.apagada = True
        self.acesa = False

def ascenderLuz(lampada):
    if(lampada.apagada == True and lampada.acesa == False):
        lampada.acesa = True
        lampada.apagada = False
        print("Lampada acesa!")
    else:
        print("Essa lampada já está acesa!")

def pagarLuz(lampada):
    if(lampada.apagada == False and lampada.acesa == True):
        lampada.acesa = False
        lampada.apagada = True
        print("Lampada apagada!")
        
    else:
        print("Essa lampada já está desligada!")

def exibirLuz(lampada):
    if(lampada.acesa == True and lampada.apagada == False):
        print("A lampada está acesa!")
    else:
        print("A lampada está apagada!")


lampada1 = Lampada()
lampada1.acesa = True
lampada1.apagada = False
exibirLuz(lampada1)

