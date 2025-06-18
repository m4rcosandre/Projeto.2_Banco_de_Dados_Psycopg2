#Biblioteca padrão
import psycopg2

 
# Conectar ao banco padrão 'postgres'
def conectar_banco(nome_banco):
  try:
    conexao = psycopg2.connect(
      dbname = nome_banco,
      user = "postgres",
      password = "dedeuogostoso123",
      host = "localhost",
      port = "5432"
    )
    print(f"Conectado ao banco {nome_banco} com sucesso!")
    return conexao
  except Exception as e:
    print(f"Erro ao conectar ao banco. {e}")
    return None
  

def criar_tabela(conexao):
  cursor = conexao.cursor()
  cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas(
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,                   
    contato NUMERIC             
      )
  """)
  conexao.commit()
  cursor.close()
  
def inserir_valores(conexao):
  nome = input('Nome: ')
  email = input('email: ')
  contato = input('contato: ')
  cursor = conexao.cursor()
  cursor.execute("""INSERT INTO pessoas (nome, email, contato) 
                 VALUES (%s, %s, %s)""", (nome, email, contato)) 
  conexao.commit()
  cursor.close()

def deletar_valor(conexao):
  id_alvo = input('Digite o ID da pessoa que deseja deletar: ')
  cursor = conexao.cursor()
  cursor.execute("""DELETE FROM pessoas WHERE id = %s""", (id_alvo,))

  conexao.commit()
  cursor.close()
  print("registro deletado com sucesso.")


def atualizar_valor(conexao):
  id_alvo = input("Diga aqui o ID da pessoa que deseja atualizar os dados")
  nome = input("Novo nome: ")
  email = input("Novo email: ")
  contato = input("Novo contato: ")

  cursor = conexao.cursor()
  cursor.execute("""UPDATE pessoas 
                 SET nome = %s, email = %s, contato = %s 
                 WHERE id = %s""", (nome,email,contato,id_alvo))
  conexao.commit()
  cursor.close()
  print("Registro atualizado com sucesso.")




nome_banco = input("Digite o nome do banco de dados existente para imprimir os dados: ")
conexao = conectar_banco(nome_banco)

criar_tabela(conexao)
inserir_valores(conexao)
atualizar_valor(conexao)
deletar_valor(conexao)