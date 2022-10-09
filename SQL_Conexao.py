import mysql.connector as bd

con = bd.connect(
    user ='root',
    password='Julianagagliano7@#',
    host='localhost',
    database='Drug_Store',
    port= 3306,
)

cursor = con.cursor()

def adicionar_dados():
    query = "INSERT INTO Funcionários(Nome,CPF,Telefone,Cargo,Salário) VALUES('Demogorgon','569.860.052-12','(24) 901739196','Estoquista',1200);"
    cursor.execute(query)
    con.commit()
    print('Dado Adicionado com Sucesso!')


def excluir_dados():
    query =  "DELETE FROM Funcionários where id=3;"
    cursor.execute(query)
    con.commit()
    print('Dado Excluído com Sucesso!')

def atualizar_dados():
    query = "UPDATE Funcionários SET Nome='Nancy Wheeler' WHERE ID='1';"
    cursor.execute(query)
    con.commit()
    print('Dado Atualizado com Sucesso!')


def mostrar_estrutura_tabela():
    query = "SHOW TABLES;"
    cursor.execute(query)
    resultado = cursor.fetchall()
    print(resultado)

def mostrar_toda_tabela():
    query = "SELECT * FROM Funcionários;"
    cursor.execute(query)
    resultado = cursor.fetchall()
    print(resultado)


adicionar_dados()
mostrar_toda_tabela()
