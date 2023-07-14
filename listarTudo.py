import tkinter as tk

def listar_tudo():
    root = tk.Tk()
    root.title("Tabela")

    referencia = ["nome", "quantidade", "numero do lote", "preço", "categoria", "sku"]

    cabecalho = [[referencia[j] for j in range(6)] for i in range(1)]

    for i in range(1):
        for j in range(6):
            label = tk.Label(root, text=cabecalho[i][j], borderwidth=1, relief="solid", width=15, height=2)
            label.grid(row=i, column=j)
    
    # Criar uma lista de listas para representar os dados da tabela
    dados = [["Celula ({}:{})".format(i, j) for j in range(6)] for i in range(1)]
    
    # Criar os rótulos da tabela
    for i in range(1):
        for j in range(6):
            label2 = tk.Label(root, text=dados[i][j], borderwidth=1, relief="solid", width=12, height=2)
            label2.grid(row=i+2, column=j)  # Adicionando 2 ao valor de 'row' para posicionar abaixo da primeira tabela
    
    root.mainloop()

listar_tudo()
