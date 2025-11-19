import psycopg2 as psy

try:
    con = psy.connect(
        host = "localhost",
        database= "mauricio",
        user="postgres",
        password = "postgres"
    )
except Exception as e:
    print(f"Erro ao conectadar no banco de dados: {e}")