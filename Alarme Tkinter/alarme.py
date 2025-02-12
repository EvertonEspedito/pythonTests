import tkinter as tk
from tkinter import ttk
import datetime
import time
import os

def alarme():
    while True:
        set_alarm = f'{hour_combo.get()}:{minute_combo.get()}:{second_combo.get()}'
        time.sleep(1)
        alarm_time = datetime.datetime.now().strftime('%H:%M:%S')
        if set_alarm == alarm_time:
            os.system('mpg123 alarm.mp3')#colocar nome do alarme!!!

# Criação da janela principal
root = tk.Tk()

# Adiciona um título ao topo da janela
tk.Label(root, text="Alarme | Everton Espedito", font=('Helvetica 18 bold')).pack(pady=10)

# Adiciona um subtítulo para indicar que o usuário deve definir o alarme
tk.Label(root, text="Definir Alarme", font=('Arial 12 bold')).pack(pady=5)

# Criação de um frame para agrupar os menus dropdown
frame = tk.Frame(root)
frame.pack(pady=10)  # Adiciona um espaçamento vertical

# Função para criar um Combobox
def create_combobox(values):
    combo = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(values)], width=5, state='readonly')
    combo.current(0)  # Define o valor inicial como 00
    return combo

# Criando Combobox para horas, minutos e segundos
hour_combo = create_combobox(24)
minute_combo = create_combobox(60)
second_combo = create_combobox(60)

# Posicionando os Combobox no frame
hour_combo.pack(side=tk.LEFT, padx=5)
minute_combo.pack(side=tk.LEFT, padx=5)
second_combo.pack(side=tk.LEFT, padx=5)

#Botão
button = tk.Button(root, text="Definir Alarme", font=('Helvetica 12'),command=alarme).pack(pady=20)

# Configuração da janela principal
root.title('Alarme | Everton Espedito')  # Define o título da janela
root.geometry("600x350")  # Define o tamanho da janela
root.resizable(width=0, height=0)  # Impede redimensionamento da janela

# Mantém a janela aberta até que o usuário a feche
root.mainloop()
