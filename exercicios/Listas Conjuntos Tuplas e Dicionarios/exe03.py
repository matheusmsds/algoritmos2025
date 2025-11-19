desenvolvedor1 = {"Python", "Java", "C++", "JavaScript"}
desenvolvedor2 = {"JavaScript", "Ruby", "Python", "Go"}


def analisar_linguagens(conjunto1, conjunto2):
    print("\n--- Análise de Linguagens ---")
    print(f"Desenvolvedor 1: {conjunto1}")
    print(f"Desenvolvedor 2: {conjunto2}\n")
    
    em_comum = conjunto1.intersection(conjunto2)
    print(f"Linguagens em comum (interseção): {em_comum}")

    todas_conhecidas = conjunto1.union(conjunto2)
    print(f"Todas as linguagens conhecidas pelos dois (união): {todas_conhecidas}")

    diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
    print(f"Linguagens que só um dos dois conhece (diferença simétrica): {diferenca_simetrica}")

def consultar_linguagem(conjunto,linguagem):
    if (linguagem in conjunto):
        return "Sim"
    else:
        return "Não"
def main():
    linguagem_para_consultar = "C++"
    presente_dev1 = consultar_linguagem(desenvolvedor1, linguagem_para_consultar)
    print(f'\n• Consulta: "{linguagem_para_consultar}" está presente no conjunto do desenvolvedor 1? {presente_dev1}')

    linguagem_para_consultar_2 = "Go"
    presente_dev2 = consultar_linguagem(desenvolvedor2, linguagem_para_consultar_2)
    print(f'• Consulta: "{linguagem_para_consultar_2}" está presente no conjunto do desenvolvedor 2? {presente_dev2}')

    linguagem_para_consultar_3 = "Cobol"
    presente_dev1_3 = consultar_linguagem(desenvolvedor1, linguagem_para_consultar_3)
    print(f'• Consulta: "{linguagem_para_consultar_3}" está presente no conjunto do desenvolvedor 1? {presente_dev1_3}')

    analisar_linguagens(desenvolvedor1, desenvolvedor2)

main()