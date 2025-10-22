from funcs import incluir_livro, alterar_livro, excluir_livro,mostrar_livros
while (True):
    print("""
    |------------ (MENU LIVROS) -------------|
    | 1 - INCLUIR LIVRO                      |
    | 2 - VER LIVROS                         |
    | 3 - ALTERAR LIVRO                      |
    | 4 - EXCLUIR LIVRO                      |
    | 0 - SAIR                               |
    |----------------------------------------|
""")
    op = int(input("Digite uma opção: "))

    if(op == 1):
        incluir_livro()
    elif(op == 2):
        mostrar_livros()
    elif(op == 3):
        alterar_livro()
    elif(op == 4):
        excluir_livro()
    elif(op == 0):
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")