#Biblioteca padrão
import psycopg2

#conectando ao banco padrão
try:
  conn = psycopg2.connect(

    dbname = "postgres",
    user = "postgres",
    password = "dedeuogostoso123",
    host = "localhost",
    port = "5432"
  )
  conn.autocommit = True
  cur = conn.cursor()
except:
  print("Erro ao se conectar ao banco.")
  
def criar_banco(nome_database):
  try:
    cur.execute(F"CREATE DATABASE{nome_database}")

    print("Banco de dados criado com sucesso!")
    cur.close()
    conn.close()
  except Exception as e:
    print(f"Erro ao criar um banco de dados!: {e}")
  





def conectar(nome_banco_novo):

  try:
    conn = psycopg2.connect(

      dbname = nome_banco_novo,
      user = "postgres",
      password = "dedeuogostoso123",
      host = "localhost",
      port = "5432"
    )

    cur = conn.cursor()
    print(f"Banco de dados {nome_banco_novo} conectado!")
    return conn,cur
  except psycopg2.Error as n:
    print(f'Erro ao se conectar ao banco {n}')
    return None, None