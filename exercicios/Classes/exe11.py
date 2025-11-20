from datetime import date
class DataNascimento:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0
        

class Pessoa:
    def __init__(self):
        self.nome = ""
        self.datanascimento = DataNascimento()

def calcularIdade(pessoa):
    hoje = date.today()
    
    ano = pessoa.datanascimento.ano
    mes = pessoa.datanascimento.mes
    dia = pessoa.datanascimento.dia
    
    idade = hoje.year - ano
    
    if(hoje.month < mes):
        idade -= 1
    elif(hoje.month == mes):
        if(hoje.day < dia):
            idade -= 1
    return idade

def ExibirPessoa(pessoa):
        print(f"Nome: {pessoa.nome}")
        print(f"Data de nascimento: {pessoa.datanascimento.dia}/{pessoa.datanascimento.mes}/{pessoa.datanascimento.ano}")
        print(f"Idade atual: {calcularIdade(pessoa)}")


def lerDados():
   pessoa = Pessoa()
   pessoa.nome = input("Informe o nome: ")
   data_nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
   string = data_nasc.split("/")
   
   pessoa.datanascimento.dia = int(string[0])
   pessoa.datanascimento.mes = int(string[1])
   pessoa.datanascimento.ano = int(string[2])
   
   return pessoa

ExibirPessoa(lerDados())