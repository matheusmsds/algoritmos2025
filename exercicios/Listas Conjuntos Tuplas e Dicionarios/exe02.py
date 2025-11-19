funcionarios = [
("Ana", 30, 4500.00),
("Bruno", 25, 3800.50),
("Carlos", 40, 5200.75),
("Diana", 35, 4100.00)
]

def retornarMaiorSalario(lista:list):
    for i in range(0, len(lista)):
        if(i == 0):
            salario = lista[i][2]
        if(lista[i][2] > salario):
            funcionario = lista[i]
    if len(lista) > 0:
        return funcionario
    return 0.0
    
def mediaSalarial(lista:list):
    soma = 0
    media = 0
    for i in range(0, len(lista)):
        soma += lista[i][2]
    if len(lista) > 0:
        media = round(soma / len(lista), 2)
        return media
    return 0.0

def encontrarFuncionario(lista:list, nome:str):
    for i in range(0, len(lista)):
        if(nome == lista[i][0]):
            busca = lista[i]
            return busca
    return "Usúario não encontrado"
    
def main():
    maior_salario = retornarMaiorSalario(funcionarios)
    media = mediaSalarial(funcionarios)
    encontrar_funcionario = encontrarFuncionario(funcionarios, "Ana")
    
    print(f"Funcionario com maior salário: {maior_salario}\n")
    print(f"Média salárial dos funcionários: {media}\n")
    print(f"Funcionário encontrado: {encontrar_funcionario}\n")

main()