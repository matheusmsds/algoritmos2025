from datetime import date

class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

class Cliente:
    def __init__(self):
        self.nome = ""
        self.data_nascimento = Data()

class ContaBancaria:
    def __init__(self):
        self.cliente = Cliente()
        self.saldo = 0.0
        self.data_abertura = Data()

def dataAbertura(data):
    hoje = date.today()
    data.dia = hoje.day
    data.mes = hoje.month
    data.ano = hoje.year
    return data

def lerData():
    data = Data()
    string_data = input("Informe a data de nascimento do cliente (dd/mm/aaaa): ")
    vetor = string_data.split("/")
    data.dia = int(vetor[0])
    data.mes = int(vetor[1])
    data.ano = int(vetor[2])
    return data

def lerCliente():
    cliente = Cliente()
    cliente.nome = input("Informe o nome do cliente: ")
    cliente.data_nascimento = lerData()
    return cliente

def lerConta():
    conta = ContaBancaria()
    print("\n--- Criação da Conta Bancária ---")
    conta.data_abertura = dataAbertura(Data())
    conta.cliente = lerCliente()
    conta.saldo = float(input("Saldo inicial: R$ "))
    return conta

def exibirContaBancaria(conta):
    print("\n==============================")
    print("Nome do Cliente:", conta.cliente.nome)
    print("Data de Nascimento: {}/{}/{}".format(
        conta.cliente.data_nascimento.dia,
        conta.cliente.data_nascimento.mes,
        conta.cliente.data_nascimento.ano))
    print("Saldo: R$ {:.2f}".format(conta.saldo))
    print("Data de Abertura: {}/{}/{}".format(
        conta.data_abertura.dia,
        conta.data_abertura.mes,
        conta.data_abertura.ano))
    print("==============================")
