
# Exercício 01: Um telefone celular precisa ser representado em um programa de computador. Sabe-se que este
# telefone possui uma marca, um modelo, um ano de fabricação e um preço. Implemente uma estrutura para
# representar os telefones celulares. Crie três celulares, solicite os dados ao usuário para cada um e apresente-
# os na tela.

class Telefone:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano_fabricacao = 0
        self.preco = 0.0

def obterTelefone():
    telefone = Telefone()
    telefone.marca = input("Informe a marca do celular: ")
    telefone.modelo = input("Informe o modelo do celular: ")
    telefone.ano_fabricacao = int(input("Informe o ano de fabricacao do celular: "))
    telefone.preco = float(input("Informe o preço do celular: "))
    print()
    return telefone

def mostrarTelefone(telefone):
    print(f"Marca: {telefone.marca}\nModelo: {telefone.modelo}\nAno de fabricação: {telefone.ano_fabricacao}\nPreço: {telefone.preco}\n")

qtd = int(input("Informe a quantide de celulares que deseja cadastrar: "))

listatelefones = [Telefone()] * 3

for cont in range(0, len(listatelefones)):
    print(f"{cont + 1}º Celular")
    listatelefones[cont] = obterTelefone()

for cont in range(0, len(listatelefones)):
    print(f"{cont + 1}º Celular")
    mostrarTelefone(listatelefones[cont],cont)