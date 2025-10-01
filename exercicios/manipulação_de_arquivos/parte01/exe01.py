def escrever_5frutas():
    vetor = [""] * 5

    for i in range(0, len(vetor)):
        vetor[i] = input(f"Informe a {i+1}º fruta: ")

    string_formatada = ""
    for i in range(0, len(vetor)):
        string_formatada += f"{vetor[i]}\n"

    arquivo = open("frutas.txt", "w", encoding="utf8")
    arquivo.write(string_formatada)

    arquivo.close()

def ler_frutas():
    arquivo = open("frutas.txt", "r", encoding="utf8")
    linhas = arquivo.readlines()

    for i in range(0, len(linhas)):
        print(f"Eu adoro a fruta: {linhas[i].strip()}")
    arquivo.close()    

def adicionar_3frutas():
    vetor = [""] * 3

    for i in range(0, len(vetor)):
        vetor[i] = input(f"Informe a {i+1}º fruta: ")

    string_formatada = ""
    for i in range(0, len(vetor)):
        string_formatada += f"{vetor[i]}\n"

    arquivo = open("frutas.txt", "a", encoding="utf8")
    arquivo.write(string_formatada)

    arquivo.close()

def apagar_frutas():
    arquivo = open("frutas.txt", "w", encoding="utf8")
    arquivo.write("Desculpe, esqueci tudo 😅")
    arquivo.close()

apagar_frutas()