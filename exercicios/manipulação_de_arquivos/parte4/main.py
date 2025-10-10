import random

numero = random.randint(1, 100)
arquivo = "jogo.txt"

escrever_n = open(arquivo, "w", encoding="utf8")
escrever_n.write(f"{numero}")
escrever_n.close()

tentativas = 0
acertou = False

while (not acertou):
    try:
        chute = int(input("Informe um número: "))
        tentativas += 1

        if(chute == numero):
            resultado = "Acertou"
            acertou = True
        elif(chute < numero):
            resultado = "Maior"
        else:
            resultado = "Menor"
        escrever_resultado = open(arquivo, "a", encoding="utf8")
        escrever_resultado.write(f"\nTentativa {tentativas}: {chute} -> {resultado}")
        escrever_resultado.close()
        print(resultado)
    except ValueError:
        print("Digite um número válido")

print(f"\nVocê acertou em {tentativas} tentativas!")

exibir_conteudo = open(arquivo, "r", encoding="utf8")
print(exibir_conteudo.read())
exibir_conteudo.close()