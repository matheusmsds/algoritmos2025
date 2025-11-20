# Uma pessoa possui um nome, uma data de nascimento (dia, mês e ano) e uma hora de
# nascimento (hora e minuto). Implemente um programa que seja capaz de representar uma pessoa (utilizando
# registros).

class DataNascimento:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

class HoraNascimento:
    def __init__(self):
        self.hora = 0
        self.minutos = 0

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.datanascimento = DataNascimento()
        self.horanascimento = HoraNascimento()
    def ExibirPessoa(self):
        print(f"Nome: {self.nome}")
        print(f"Data de nascimento: {self.datanascimento.dia}/{self.datanascimento.mes}/{self.datanascimento.ano}")
        print(f"Horario de nascimento: {self.horanascimento.hora}:{self.horanascimento.minutos}")


def CriarPessoa(nome,data_nascimento:str, nascimento_hora:str):
    pessoa = Pessoa()
    pegar_data = data_nascimento.split("/")
    dia = int(pegar_data[0])
    mes = int(pegar_data[1])
    ano = int(pegar_data[2])
    
    pegar_hora = nascimento_hora.split(":")
    hora = int(pegar_hora[0])
    minutos = int(pegar_hora[1])
    
    pessoa.nome = nome
    pessoa.datanascimento.dia = dia
    pessoa.datanascimento.mes = mes
    pessoa.datanascimento.ano = ano
    pessoa.horanascimento.hora = hora
    pessoa.horanascimento.minutos = minutos
    return pessoa

pessoa1 = Pessoa()
CriarPessoa(pessoa1, "João", "01/11/2000","12:00")
pessoa1.ExibirPessoa()