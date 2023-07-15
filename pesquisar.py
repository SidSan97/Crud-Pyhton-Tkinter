import tkinter as tk
from tkinter import *
from connect import *

def pesquisa():
    janela = tk.Tk()
    janela.title("Pesquisar produto")
    janela.geometry("400x380")

    texto1 = Label(janela, text="Insira nome do produto", anchor='center', font=('Arial', 15))
    texto1.place(x=15, y=20)
    entry1 = tk.Entry(janela)
    entry1.place(x=18, y=50)

    def fazerPesquisa(entry1):
        dado = entry1.get()
        result = search(dado)

        referencia = result

        dados = [[referencia[i][j] for j in range(7)] for i in range(len(referencia))]
    
        for i in range(len(referencia)):
            for j in range(7):
                label2 = tk.Label(janela, text=dados[i][j], borderwidth=0, relief="solid", width=18, height=2)
                label2.grid(row=i+2, column=j)


    botao = tk.Button(janela, text="Enviar", command=lambda i=entry1: fazerPesquisa(i))
    botao.place(x=120, y=50)

    janela.mainloop()

pesquisa()
