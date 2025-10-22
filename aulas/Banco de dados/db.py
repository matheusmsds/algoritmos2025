import psycopg2 as psy

con = psy.connect(
    host = "localhost",
    database= "algoritmos",
    user="postgres",
    password = "postgres"
)
cursor = con.cursor()
