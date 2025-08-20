def inputInt(msg:str):
    n = int(input(msg))
    return n

def ePrimo(numero):
    for i in range(2, numero):
        if(numero % i == 0):
            return False
    return True