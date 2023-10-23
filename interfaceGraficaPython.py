
# Tkinter biblioteca gráfica
# as tk referencia os objetos e classes do módulo Tkinter
import tkinter as tk
# themed Tkinter, é um conjunto de widgtes(elementos de interface)
from tkinter import ttk

def calcular_imc(peso,altura):
    imc = peso/ (altura**2)
    return imc


 # realizando a classificação da obesidade
def classificar_imc(imc):
    if imc < 18.5:
        return("Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        return("Peso normal")
    elif 25 <= imc <= 29.9:
        return("Sobrepeso")
    elif 30 <= imc <=34.9:
        return("Obsedidade Grau I")
    elif 35 <= imc <= 39.9:
        return("Obesidade Grau II")
    else:
        return("Obesidade Grau III")


def cadastrar_pessoa():

    nome = nome_entry.get()
    idade = int(idade_entry.get())
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    
    imc = calcular_imc(peso,altura)
    classificacao = classificar_imc(imc)

    mensagem_label.config(text=f"Nome: {nome}\n Idade: {idade}\n Peso: {peso}, kg"
    f"\n Altura: {altura} \n IMC: {imc:.2f}")
    classificacao_label.config(text=f"A classificação é: {classificacao}")



# cria a janela principal
root = tk.Tk()
root.title("Inova Uniesp")
# defina o tamanho da janela
root.geometry("500x500")
#defina a cor de fundo de tela
root.configure(bg="pink")

# defina fonte
fonte = ("Arial", 12)

#cria os widgets
nome_label = ttk.Label(root, text=" Nome:", font = fonte, background = "pink")
nome_entry = ttk.Entry(root, font = fonte, width = 30)
idade_label = ttk.Label(root, text=" Idade:", font = fonte, background = "pink")
idade_entry = ttk.Entry(root, font = fonte, width = 30)
peso_label = ttk.Label(root, text=" Peso(kg):", font = fonte, background = "pink")
peso_entry = ttk.Entry(root, font = fonte, width = 30)
altura_label = ttk.Label(root, text=" Altura(m):", font = fonte, background = "pink")
altura_entry = ttk.Entry(root, font = fonte, width = 30)
mensagem_label = ttk.Label(root, text="",font=fonte,  background = "pink")
classificacao_label = ttk.Label(root, text="",font=fonte,  background = "pink")

#Adiciona um botão e posiciona na janela(widgets do botão)
botao = ttk.Button(root, text="Calcular IMC",command=cadastrar_pessoa)

#Ajusta a posição Geometricamente na tela
nome_label.grid(row=0, column=0, padx=10, pady=5)
nome_entry.grid(row=0, column=1, padx=10, pady=5)
idade_label.grid(row=1, column=0, padx=10, pady=5)
idade_entry.grid(row=1, column=1, padx=10, pady=5)
peso_label.grid(row=2, column=0, padx=10, pady=5)
peso_entry.grid(row=2, column=1, padx=10, pady=5)
altura_label.grid(row=3, column=0, padx=10, pady=5)
altura_entry.grid(row=3, column=1, padx=10, pady=5)
botao.grid(row=4, column=0, columnspan=2,padx=20,pady=20)
mensagem_label.grid(row=5,column=0, columnspan=2,pady=5)
classificacao_label.grid(row=6,column=0, columnspan=2,pady=5)

#Inicia a interface gráfica
root.mainloop()