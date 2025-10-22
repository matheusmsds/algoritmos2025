def digitar_5items():
    vetor = [0] * 5
    for i in range(0, len(vetor)):
        vetor[i] = input(f"Informe o {i + 1}º item: ")
    
    string_formatada = ""
    for i in range(0, len(vetor)):
        string_formatada += f"{vetor[i]}\n"

    arquivo = open("items.txt","w",encoding="utf8")
    arquivo.write(string_formatada)
    arquivo.close()    

def ler_items():
    arquivo = open("items.txt","r",encoding="utf8")
    items = arquivo.readlines()

    for i in range(0, len(items)):
        print(f"{i+1} - {items[i].strip()}")
    arquivo.close()

def deseja_add_items():
    while (True):
        op = input("Deseja adicionar mais items? (s/n)\n").strip()
        if(op != "s"):
            print("Ok! finalizando programa...")
            break
        
        tam = int(input("Informe quantos itens você quer adicionar: "))

        vetor = [0] * tam
        for i in range(0, len(vetor)):
            vetor[i] = input(f"Informe o {i + 1}º item: ")
        
        string_formatada = ""
        for i in range(0, len(vetor)):
            string_formatada += f"{vetor[i]}\n"
        arquivo = open("items.txt","a",encoding="utf8")
        arquivo.write(string_formatada)
        arquivo.close()

deseja_add_items()