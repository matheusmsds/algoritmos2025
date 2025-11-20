class Matematica:
    def __init__(self):
        self.operacao = ""
        self.valor1 = 0
        self.valor2 = 0

def getCalculo(valor1, valor2, operacao):
    resultado = 0
    matematica = Matematica()
    matematica.valor1 = valor1
    matematica.valor2 = valor2
    matematica.operacao = operacao
    
    if(operacao == "+"):
        resultado = valor1 + valor2 
    elif(operacao == "-"):
        resultado = valor1 - valor2
    elif(operacao == "*"):
        resultado = valor1 * valor2
    elif(operacao == "/"):
        if(valor2 != 0):
            resultado = valor1 / valor2
        else:
            return "Erro | divisão por zero"
    else:
        return "Erro: Operação inválida. Use '+', '-', '*' ou '/'."
    return resultado

a = getCalculo(2,2,"+")
b = getCalculo(2,2,"-")
c = getCalculo(2,2,"*")
d = getCalculo(2,2, "/")

print(a)
print(b)
print(c)
print(d)