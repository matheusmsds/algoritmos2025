from db import con

def mostrar_livros():
    cursor = con.cursor()
    
    cursor.execute("SELECT id, titulo, autor, ano_publicacao FROM livros")
    livros = cursor.fetchall()
    if not livros:
        print("Nenhum livro encontrado.")
    else:
        for livro in livros:
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Data de Lançamento: {livro[3]}")
            print("-" * 30)
    
    a = input("continuar...")
    cursor.close()

def incluir_livro():
    cursor = con.cursor()
    cmd = "INSERT INTO livros(titulo,autor,ano_publicacao) VALUES (%s,%s,%s)"
    qtd = int(input("Informe a quantidade de registros: "))

    for i in range(0, qtd):
        print(f"Informe o {i + 1} registro\n")
        titulo = input("Informe o titulo do livro: ")
        autor = input("Informe o autor do livro: ")
        ano = input("Informe o ano do livro fomarto (AAAA-MM-DD): ")
        
        valores = (titulo,autor,ano)
        cursor.execute(cmd, valores)

    con.commit()
    cursor.close()

def excluir_livro():
    cursor = con.cursor()
    cmd = "DELETE FROM livros WHERE id = %s"
    id_livro = input("Informe o ID do livro que deseja deletar: ")
    cursor.execute(cmd, id_livro)

    print(f"Livro {id_livro} deletado com sucesso.")
    con.commit()
    cursor.close()

def alterar_livro():
    cursor = con.cursor()
    id_livro = int(input("Informe o ID do livro que deseja alterar: "))
    print("""
    |------------ (ALTERAR LIVRO) -----------|
    | 1 - TITULO                             |
    | 2 - AUTOR                              |
    | 3 - DATA DE LANÇAMENTO                 |                           |
    |----------------------------------------|
""")
    opcao = input("Escolha uma opção: ")

    if(opcao == '1'):
        novo_titulo = input("Informe o novo título do livro: ")
        cmd = "UPDATE livros SET titulo = %s WHERE id = %s"
        valores = (novo_titulo, id_livro)

    elif(opcao == '2'):
        novo_autor = input("Informe o novo autor do livro: ")
        cmd = "UPDATE livros SET autor = %s WHERE id = %s"
        valores = (novo_autor, id_livro)

    elif(opcao == '3'):
        nova_data = input("Informe a nova data de lançamento (YYYY-MM-DD): ")
        cmd = "UPDATE livros SET data_lancamento = %s WHERE id = %s"
        valores = (nova_data, id_livro)

    else:
        print("Opção inválida.")
        cursor.close()
        return

    cursor.execute(cmd, valores)
    con.commit()
    cursor.close()

    print(f"Livro com ID {id_livro} foi alterado com sucesso.")