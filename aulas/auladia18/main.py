"""
# MATRIZ

# linhas = 3
# colunas = 4
# matriz = [0] * linhas

# for i in range(0, len(matriz)):
#     matriz[i] = [0] * colunas

# print(matriz)

# LISTA

# lista = []
# lista.append("Ahhh")
# lista.append(1)
# lista.insert(1,"oi")
# lista.pop(1)
# lista.remove("oi")
# print(lista)

# exercicio basico

# lista = []
# for i in range(0, 6):
#     nome = input(f"Informe o {i + 1}º nome:")
#     lista.append(nome)

# apagar_nome = input("Qual usúario deseja remover da lista: ")
# lista.remove(apagar_nome)

# print("Lista Final: ")
# print(f"Nome apagado: {apagar_nome}\n")

# for i in range(0, len(lista)):
#     print(lista[i], end=" | ")

# lista = []
# i = 0
# while(True):
#     i += 1
#     nome = input(f"Informe o {i}º nome:").strip()
#     if(nome == ""):
#         break
#     lista.append(nome)

# apagar_nome = input("Qual usúario deseja remover da lista: ").strip()
# lista.remove(apagar_nome)

# for i in range(0, len(lista)):
#     print(lista[i], end=" | ")

# TUPLA
# tupla = ("A", 1, 1.0, 40.10,False, [1,3,4,5])

# print(tupla)

# TUPLA EXERCICIO


# nome_produto = input("Informe o nome do produto: ").strip()
# preco_produto = float(input("Informe o preço do produto: "))
# qtd_produto = int(input("Informe a quantidade em estoque: "))

# produto = (nome_produto, preco_produto, qtd_produto)
# print("")
# print(f"Tamanho da tupla: {len(produto)}")
# print("")

# for i in range(0, len(produto)):
#     print(produto[i], end=" | ")

# print("")


# CONJUNTOS
# conjunto = set()
# conjunto = {[1,2,3,4,5,6]}
# a = {1,2,3,4,5,6}
# a.add(7)

# b = {4,5,2,1,10,90,9.56}
# x = {1,2}


# uniao = a.union(b)
# inter = a.intersection(b)
# difereA = a - b
# difereB = b - a


# subc = x.issubset(a)
# per = 8 in a

# print(a)
# print()
# print(b)
# print()
# print(uniao)
# print()
# print(inter)
# print()
# print(difereA)
# print()
# print(difereB)
# print()
# print(subc)
# print()
# print(per)


# #EXERCICIO CONJUNTO

# turma_a = {"Ana","Beto","Carlos","Duda"}
# turma_b = {"Carlos","Edu","Fernanda", "Ana"}

# interc = turma_a.intersection(turma_b)
# difere = turma_a.difference(turma_b)
# uniao = turma_a.union(turma_b)

# print()

# print(f"Turma A: {turma_a}")
# print(f"Turma B: {turma_b}")

# print()
# print(f"Interseção de A em B: {interc}")
# print(f"Somente alunos da turma A:  {difere}")
# print(f"União das turmas A e B: {uniao}")

# DICIONARIO

# dic = {}
pessoa = {
    "nome" : "Maria",
    "idade" : 20
}

for chave, valor in pessoa.items():
    print(f"{chave} : {valor}")
"""

# EXERCICIO DICIONARIO
aluno = {
    "nome" : "Maria",
    "idade" : 20,
    "curso" : "Engenharia de Software"
}

for chave, valor in aluno.items():
    print(f"{chave} : {valor}")
print()

aluno["idade"] = 19
aluno["nota"] = 70

print()
for chave, valor in aluno.items():
    print(f"{chave} : {valor}")

print()
aluno.pop("curso")
print()

for chave, valor in aluno.items():
    print(f"{chave} : {valor}")