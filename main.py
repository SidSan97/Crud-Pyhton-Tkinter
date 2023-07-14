import tkinter as tk
from tkinter import *
from listarTudo import *
from connect import *

def obter_valores():
    #Obter os valores dos campos de entrada
    valor1 = entry1.get()
    valor2 = entry2.get()
    valor3 = entry3.get()
    valor4 = entry4.get()
    valor5 = entry5.get()
    valor6 = entry6.get()

    insert(valor1, valor2, valor3, valor4, valor5, valor6)

def exibirTudo():
    listar_tudo()

janela = tk.Tk()
janela.title("Exemplo de Janela")
janela.geometry("400x380")

# Criação dos campos de entrada
texto1 = Label(janela, text="Insira nome do produto", anchor='center')
texto1.place(x=10, y=40)
entry1 = tk.Entry(janela)
entry1.place(x=10, y=70)


texto2 = Label(janela, text="Quantidade", anchor='center')
texto2.place(x=220, y=40)
entry2 = tk.Entry(janela)
entry2.place(x=220, y=70)

texto3 = Label(janela, text="Numero do lote", anchor='center')
texto3.place(x=10, y=110)
entry3 = tk.Entry(janela)
entry3.place(x=10, y=130)

texto4 = Label(janela, text="Preço em R$", anchor='center')
texto4.place(x=220, y=110)
entry4 = tk.Entry(janela)
entry4.place(x=220,y=130)

texto5 = Label(janela, text="Tipo do Produto", anchor='center')
texto5.place(x=10, y=180)
entry5 = StringVar()
entry5.set( " " )
item_menu = OptionMenu(janela, entry5, "Laticinios", "Legumes", "Bebidas", "Calçados", "Vestuário", 
                    "Higiene","Eletrodomésticos","Eletrônicos" ,"Outros")
item_menu.place(x=10, y=210)

texto6 = Label(janela, text="SKU", anchor='center')
texto6.place(x=220, y=180)
entry6 = tk.Entry(janela)
entry6.place(x=220,y=210)


# Botão para obter os valores dos campos de entrada
botao = tk.Button(janela, text="Enviar", command=obter_valores)
botao.place(x=150, y=290)

botao2 = tk.Button(janela, text="Ver Tudo", command=exibirTudo)
botao2.place(x=10, y=10)

janela.mainloop()
