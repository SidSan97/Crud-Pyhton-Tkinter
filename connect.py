import mysql.connector

def conect():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud_python"
    )

    return conexao


def insert(prod_nome, qtd, num_lote, preco, tip_prod, sku):
    conexao = conect()

    # Criar um objeto cursor para executar as consultas SQL
    cursor = conexao.cursor()

    # Definir a consulta SQL de INSERT com os valores a serem inseridos
    sql = "INSERT INTO produto (prod_nome, quantidade, num_lote, preco, tipo_prod, sku) VALUES (%s, %s, %s, %s, %s, %s)"

    # Definir os valores a serem inseridos
    valores = (prod_nome, qtd, num_lote, preco, tip_prod, sku)

    # Executar a consulta SQL com os valores
    cursor.execute(sql, valores)

    # Confirmar as alterações no banco de dados
    conexao.commit()

    # Exibir mensagem de sucesso
    print("Dados inseridos com sucesso!")

    cursor.close()
    conexao.close()

def getAll():
    conexao = conect()
    dados = []

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produto")

    resultados = cursor.fetchall()

    for linha in resultados:
        dados.append(linha)

    cursor.close()
    conexao.close()

    return dados

def delete(id):
    conexao = conect()
    cursor = conexao.cursor()

    sql = "DELETE FROM produto WHERE id=%s"  

    valores = (id,)  
    cursor.execute(sql, valores)
    conexao.commit()
    print("Deletado com sucesso")

    cursor.close()
    conexao.close()


def numLinha():
    conexao = conect()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM produto")
    row_count = cursor.fetchone()[0]

    return row_count

