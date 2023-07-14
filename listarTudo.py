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
            label2.grid(row=i+8, column=j)  # Adicionando 2 ao valor de 'row' para posicionar abaixo da primeira tabela

        # Criação do botão para cada linha
        botao = tk.Button(root, text="Excluir", command=lambda i=dados[i][0]: botao_clicado(i))
        botao.grid(row=i+8, column=7)

    def botao_clicado(indice):
        #print("Botão", indice, "clicado")
        delete(indice)

    root.mainloop()

listar_tudo()
