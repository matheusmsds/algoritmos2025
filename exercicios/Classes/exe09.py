class Televisao:
    def __init__(self):
        self.polegadas = 0
        self.marca = ""
        self.status = False
        self.canal = 0
        self.volume = 0
def criarTv(tv, marca, polegadas):
    tv = Televisao()
    tv.marca = marca
    tv.polegadas = polegadas
    tv.status = False
    tv.canal = 0
    tv.volume = 0
    return tv

def lerDadosTV(tv):
    tv.marca = input("Marca da tv: ")
    tv.polegadas = int(input("Polegadas da tv: "))
    ligada = input("Tv ligada ou desligada: ").lower().strip()
    if(ligada == "sim"):
        tv.status = True
    else:
        tv.status = False
    tv.canal = int(input("Qual o canal: "))
    tv.volume = int(input("Qual o volume da tv: "))

def exibirTV(tv):
    print(f"Dados da TV {tv.marca}")
    print(f"Marca: {tv.marca}")
    print(f"Polegadas: {tv.polegadas}")
    if(tv.status):
        print("Status: Ligada")
    else:
        print("Status: Desligada")
    print(f"Canal da tv: {tv.canal}")
    print(f"Volume da tv: {tv.volume}") 

def ligar(tv):
    tv.status = not(tv.status)
    if(tv.status == True):
        tv.canal = 1

def desligar(tv):
    tv.status = False
    tv.canal = 0

def aumentarCanal(tv):
    if(tv.canal < 90):
        tv.canal += 1

def mudarCanal(tv, canal):
    if(canal < 90):
        tv.canal = canal

def aumentarVolume(tv):
    tv.volume += 1
def diminuirVolume(tv):
    tv.volume -= 1

