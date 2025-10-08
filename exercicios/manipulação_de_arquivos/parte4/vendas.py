arquivo = open("vendas.txt", "r", encoding="utf8")
conteudo = arquivo.readlines()

data = input("Informe a data: ").strip()
soma_datas = 0
for i in range(0, len(conteudo)):
    linhas = conteudo[i].split(",")
    if(linhas[2]):
        linhas[2] = float(linhas[2])
    if(linhas[0] == data):
        print(f"{linhas[0]} - {linhas[2]}", end="")
        soma_datas += linhas[2]

print(f"Soma: {soma_datas}")

arquivo.close()