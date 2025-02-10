import tkinter as tk
from tkinter import Label,Frame, Entry, Button

def calcula_imc():
    imc = float(peso.get())/(float(altura.get())* float(altura.get()))
    if imc < 18.5:
        resultado['text'] = f"Seu IMC é: {imc:.2f}, Você está abaixo do peso"
    elif imc < 25:
        resultado['text'] = f"Seu IMC é: {imc:.2f}, Você está no peso normal"
    elif imc < 30:
       resultado['text'] = f"Seu IMC é: {imc:.2f}, Você está acima do peso"
    else:
        resultado['text'] = f"Seu IMC é: {imc:.2f}, Você está obeso"
        
janela = tk.Tk()


frame = Frame(janela, 
    padx=40,
    pady=40).grid(column=1,row=1)

Label( frame,
    text="Para saber o seu IMC, Digite os valores nos campos abaixo:",
    pady=40,
    padx=40,
    font=("Arial", 11, "bold"),
      ).grid(column=1, row=1,columnspan=2)

Label(frame,
      text="Altura (em metros EX: 1.90):",
      font=("Arial", 10, "bold"),
      ).grid(column=1, row=2)
altura = Entry(frame)
altura.grid(column=2, row=2)

Label(frame,
      text="Peso (em KG EX: 80):",
      font=("Arial", 10, "bold"),
      ).grid(column=1, row=3)
peso = Entry(frame)
peso.grid(column=2, row=3)

Button(frame, text='Calcular', borderwidth=3,command=calcula_imc).grid(
    column=1, 
    row=4, 
    columnspan=2)

resultado = Label(frame,font=("Arial", 10, "bold"))
resultado.grid(column=1, row=5, columnspan=2)

janela.title('Calculadora de IMC')
janela.geometry("500x250")
janela.resizable(width=0, height=0)
janela.mainloop()