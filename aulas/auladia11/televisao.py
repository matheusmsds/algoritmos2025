class Televisao:
    def __init__(self):
        self.status = False
        self.canal = 0
        self.volume = 0

def ligar(tv):
    tv.status = not(tv.status)
    if(tv.status == True):
        tv.canal = 1

def desligar(tv):
    tv.status = False
    tv.canal = 0

def aumentarCanal(tv):
    if(tv.canal < 5):
        tv.canal += 1

def mudarCanal(tv, canal):
    if(canal < 5):
        tv.canal = canal

def aumentarVolume(tv):
    tv.volume += 1
def diminuirVolume(tv):
    tv.volume -= 1


tv1 = Televisao()

