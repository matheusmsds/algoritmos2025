# Exercício 05: Imagine uma lâmpada que possa ter três estados: apagada, acesa e meia-luz. Estes estados são
# representados por um valor de 0 a 100, onde 0 representa o estado apagado, de 80 a 100 representa o estado
# aceso e de 1 a 79 representa o estado meia-luz.
# Implemente um programa capaz de representar uma lâmpada conforme o enunciado.
# Implemente uma função chamada criarLampada que crie uma lâmpada e solicite a intensidade da lâmpada,
# retornando o objeto criado.
# Implemente um procedimento chamado exibirLampada que recebe uma lâmpada como parâmetro e
# apresente na tela se a lâmpada está apagada, acesa ou em meia-luz.

class Lampada:
    def __init__(self):
        # Garante que a intensidade esteja entre 0 e 100
        self.intensidade = 0
             
def exibirLampada(lampada):
    if (lampada.intensidade == 0):
        estado = "Apagada"
    elif(lampada.intensidade >= 1 and lampada.intensidade <= 79):
        estado = "Em meia-luz"
    elif(lampada.intensidade >= 80 and lampada.intensidade <= 100):
        estado = "Acesa"
    else:
        estado = "Valor inválido"

    print(f"A lâmpada está {estado} (intensidade: {lampada.intensidade})")

def ligar(lampada):
    lampada.intensidade = 100
    print("A lâmpada foi ligada (intensidade 100).")

def desligar(lampada):
    lampada.intensidade = 0
    print("A lâmpada foi desligada (intensidade 0).")

def meiaLuz(lampada):
    lampada.intensidade = 50
    print("A lâmpada está agora em meia-luz (intensidade 50).")

def criarLampada():
    lampada = Lampada()
    lampada.intensidade = int(input("Informe a intensidade da lâmpada (0 a 100): "))
    return lampada


# Programa principal
lampada1 = criarLampada()
exibirLampada(lampada1)

print("\n------")
desligar(lampada1)
exibirLampada(lampada1)

meiaLuz(lampada1)
exibirLampada(lampada1)

ligar(lampada1)
exibirLampada(lampada1)
