from funcs import cadastrar_produto, alterar_produto, excluir_produto, listar_produtos
import os

while (True):

    print("""
    CADASTRO DE PRODUTOS
    1. Cadastrar produto
    2. Alterar produto
    3. Excluir produto
    4. Listar todos os produtos
    5. Sair
""")
    op = int(input("Digite uma opção: "))
    os.system("cls")
    if(op == 1):
        cadastrar_produto()
    elif(op == 2):
        alterar_produto()
    elif(op == 3):
        excluir_produto()
    elif(op == 4):
        listar_produtos()
    elif(op == 5):
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")