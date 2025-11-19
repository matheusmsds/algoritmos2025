from db import con

cursor = con.cursor()

def cadastrar_produto():
    nome = input("Informe o nome do produto: ")
    valor = float(input("Informe o preço do produto: "))
    data = input("Informe a data de validade do produto: ")

    try: 
        cursor = con.cursor()
        sql = """
            INSERT INTO produtos (nome, valor, data_validade) VALUES
            (%s, %s, %s)
        """
        valores = (nome, valor, data)
    
        cursor.execute(sql, valores)
        con.commit()
    except Exception as e:
        print(f"Erro ao inserir o produto {nome}: {e}")
    
    print("Registro inserido com sucesso")
    print(f"Produto {nome} inserido ")
    cursor.close()
    con.close()

def listar_produtos():
    try: 
        sql = """
           SELECT * FROM produtos
        """
        cursor.execute(sql)
        resultado = cursor.fetchall()
        
        for linha in resultado:
            print("-------------------------")
            print("ID: ", linha[0])
            print("Nome: ", linha[1])
            print("Preço: ", linha[2])
            print("Data validade: ", linha[3])
        print("-------------------------")
        

    except Exception as e:
        print(f"Erro ao fazer o select: {e}")

    
def alterar_produto():
    id = input("Informe o ID do produto: ")
    print("""
     ALTERAR PRODUTO
     1. Nome
     2. Valor
     3. Data Validade
    """)
    opcao = int("Escolha uma opção: ")

    if(opcao == 1):
        nome = input("Informe o novo nome do produto: ")
        sql = "UPDATE produtos SET nome = %s WHERE id = %s"
        valores = (nome, id)
    elif(opcao == 2):
        valor = input("Informe o novo nome do produto: ")
        sql = "UPDATE produtos SET valor = %s WHERE id = %s"
        valores = (valor, id)
    elif(opcao == 3):
        data_validade = input("Informe a nova Data de validade produto: ")
        sql = "UPDATE produtos SET data_validade = %s WHERE id = %s"
        valores = (data_validade, id)
    else:
        print("Opção inválida!")
    try:
        cursor.execute(sql, valores)
        con.commit()
    except Exception as e:
        print("Erro ao fazer a alteração desejavel!")

    print("Registro Atualizado com sucesso!")
 

def excluir_produto():
    id = input("Informe o id do produto: ")
    try: 
        
        sql = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(sql, (id,))
        con.commit()
    except Exception as e:
        print(f"Erro ao remover o produto {id} : {e}")
    print(f"Produto {id} id excluido com sucesso")
    