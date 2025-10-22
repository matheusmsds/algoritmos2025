def por_data():
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

def busca_cliente():
    arquivo = open("vendas.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    
    nome = input("Informe o nome: ").strip()
    soma_datas = 0
    count = 0
    media = 0

    for i in range(0, len(conteudo)):
        linhas = conteudo[i].split(",")
        if(linhas[2]):
            linhas[2] = float(linhas[2])
        if(linhas[1] == nome):
            print(f"{linhas[0]} - R${linhas[2]}", end="\n")
            soma_datas += linhas[2]
            count += 1
    media = soma_datas / count

    print(f"\nSoma: R${soma_datas}")
    print(f"Média dos gastos: R${media}")
    arquivo.close()

def gerar_relatorio():
    arquivo = open("vendas.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()

    total_vendas = 0
    n_vendas = 0
    
    for i in range(0, len(conteudo)):
        linhas = conteudo[i].split(",")

        if(i == 0):
            maior_faturamento = linhas[0]
            nome_cliente = linhas[1]
            maior_valor = float(linhas[2])
        
        if(float(linhas[2]) > maior_valor):
            nome_cliente = linhas[1]
            maior_faturamento = linhas[0]
            
        total_vendas += float(linhas[2])
        n_vendas += 1
        
    print("-- Relátorio de vendas --")
    print(f"Valor total de vendas: R${total_vendas}\nNúmero de vendas: { n_vendas}\nCliente que mais gastou: {nome_cliente}\nDia com maior faturamento: {maior_faturamento}\n")
    arquivo.close()

gerar_relatorio()
