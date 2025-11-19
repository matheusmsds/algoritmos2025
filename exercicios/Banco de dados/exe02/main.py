import psycopg2 as psy

try:
    con = psy.connect(
        host = "localhost",
        database= "exe02",
        user="postgres",
        password = "postgres"
    )
except Exception as e:
    print(f"Erro ao conectadar no banco de dados: {e}")
    
def InnerJoin():
    cursor = con.cursor()
    cmd_sql = """
    SELECT idcliente, nome, nomecidade FROM cliente
    JOIN cidade ON cliente.idcidade = cidade.idcidade
    """
    cursor.execute(cmd_sql)
    resultados = cursor.fetchall()
    
    print(f"Temos um total de {cursor.rowcount} resultados")
    for linha in resultados:
        print()
        print("--------------------")
        print(f"ID: {linha[0]}")
        print(f"Nome: {linha[1]}")
        print(f"Cidade: {linha[2]}")
        print("--------------------")
        print()
        
    cursor.close()
    con.close()
    
InnerJoin()