import tkinter as tk
from tkinter import *
from connect import *

def fazerPesquisa(dado):
    #a = search(dado)
    print(dado)

def pesquisa():
    janela = tk.Tk()
    janela.title("Pesquisar produto")
    janela.geometry("400x380")

    texto1 = Label(janela, text="Insira nome do produto", anchor='center', font=('Arial', 15))
    texto1.place(x=15, y=20)
    entry1 = tk.Entry(janela)
    entry1.place(x=18, y=50)
    a = entry1.get()

    botao = tk.Button(janela, text="Enviar", command=lambda i=a: fazerPesquisa(i))
    botao.place(x=120, y=50)

    janela.mainloop()