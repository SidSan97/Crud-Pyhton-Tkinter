import tkinter as tk
from connect import *

def listar_tudo():
    root = tk.Tk()
    root.title("Tabela")

    referencia = ["ID", "NOME", "QUANTIDADE", "NUMERO DO LOTE", "PREÇO", "CATEGORIA", "SKU", "OPÇÕES"]

    cabecalho = [[referencia[j] for j in range(8)] for i in range(1)]

    for i in range(1):
        for j in range(8):
            label = tk.Label(root, text=cabecalho[i][j], borderwidth=0, relief="solid", width=15, height=2, font=('Arial', 11))
            label.grid(row=i, column=j)
    
    produtos  = getAll()
    num_linha = numLinha()
    # Criar uma lista de listas para representar os dados da tabela
    dados = [[produtos[i][j] for j in range(7)] for i in range(num_linha)]
    
    # Criar os rótulos da tabela
    for i in range(num_linha):
        for j in range(7):
            label2 = tk.Label(root, text=dados[i][j], borderwidth=0, relief="solid", width=18, height=2)
            label2.grid(row=i+2, column=j)  # Adicionando 2 ao valor de 'row' para posicionar abaixo da primeira tabela

        # Criação do botão para cada linha
        btn_excluir = tk.Button(root, text="Excluir", command=lambda i=dados[i][0]: deletar_item(i))
        btn_excluir.grid(row=i+2, column=7)

        btn_editar = tk.Button(root, text="Editar", command=lambda i=dados[i][0]: editar_item(i))
        btn_editar.grid(row=i+2, column=8)

    def deletar_item(indice):
        delete(indice)

    def editar_item(indice):
        print(indice)

    root.mainloop()

