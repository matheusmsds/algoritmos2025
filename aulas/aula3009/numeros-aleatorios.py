import random

tam = int(input("Informe o tamanho do arquivo: "))
vetor = [0] * tam

for i in range(0, len(vetor)):
    vetor[i] = random.randint(1, 100)

string_formatada = ""
for i in range(0, len(vetor)):
    string_formatada += f"{vetor[i]}\n"

arquivo = open("dados.txt", "w", encoding="utf8")
arquivo.write(string_formatada)

arquivo = open("dados.txt", "r")
linhas = arquivo.readlines()

for i in range(0, len(linhas)):
    print(f"{linhas[i]}", end="")

arquivo.close()