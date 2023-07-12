import tkinter as tk
from tkinter import *
from connect import *

def obter_valores():
    # Obter os valores dos campos de entrada
    valor1 = entry1.get()
    valor2 = entry2.get()
    valor3 = entry3.get()
    valor4 = entry4.get()
    valor5 = entry5.get()
    valor6 = entry6.get()

    # Exibir os valores obtidos
    print("Valor 1:", valor1)
    print("Valor 2:", valor2)
    print("Valor 3:", valor3)
    print("Valor 4:", valor4)
    print("Valor 5:", valor5)
    print("Valor 6:", valor6)

    enviar.envioAoBD(valor1, valor2, valor3, valor4, valor5, valor6)

janela = tk.Tk()
janela.title("Exemplo de Janela")
janela.geometry("400x300")

# Criação dos campos de entrada
texto1 = Label(janela, text="Insira nome do produto", anchor='center')
texto1.place(x=10, y=10)
entry1 = tk.Entry(janela)
entry1.place(x=10, y=40)


texto2 = Label(janela, text="Quantidade", anchor='center')
texto2.place(x=220, y=10)
entry2 = tk.Entry(janela)
entry2.place(x=220, y=40)

texto3 = Label(janela, text="Numero do lote", anchor='center')
texto3.place(x=10, y=80)
entry3 = tk.Entry(janela)
entry3.place(x=10, y=100)

texto4 = Label(janela, text="Preço em R$", anchor='center')
texto4.place(x=220, y=80)
entry4 = tk.Entry(janela)
entry4.place(x=220,y=100)

texto5 = Label(janela, text="Tipo do Produto", anchor='center')
texto5.place(x=10, y=150)
entry5 = StringVar()
entry5.set( " " )
item_menu = OptionMenu(janela, entry5, "Laticinios", "Legumes", "Bebidas", "Calçados", "Vestuário", 
                       "Higiene","Eletrodomésticos","Eletrônicos" ,"Outros")
item_menu.place(x=10, y=180)

texto6 = Label(janela, text="SKU", anchor='center')
texto6.place(x=220, y=150)
entry6 = tk.Entry(janela)
entry6.place(x=220,y=180)

enviar = EnviarAoBD()

# Botão para obter os valores dos campos de entrada
botao = tk.Button(janela, text="Enviar", command=obter_valores)
botao.place(x=150, y=260)

janela.mainloop()
