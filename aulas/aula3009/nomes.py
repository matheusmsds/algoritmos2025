tamanho = int(input("Informe a quantiade de nomes: "))
vetor = [""] * tamanho

for i in range(0, len(vetor)):
    vetor[i] = input("Informe um nome: ")

string_formatada = ""
for i in range(0, len(vetor)):
    string_formatada += f"{vetor[i]}\n"

arquivo = open("nomes.txt", "w", encoding="utf8")
arquivo.write(string_formatada)

arquivo = open("nomes.txt", "r", encoding="utf8")
dados = arquivo.readlines()

for i in range(0, len(dados)):
    print(f"{dados[i]}",end="")

arquivo.close()