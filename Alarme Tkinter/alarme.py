import tkinter as tk

root = tk.Tk()

tk.Label(root,text="Alarme | Everton Espedito", font=('Helvetica 18 bold')).pack(pady=10)
tk.Label(root,text="Definir Alarme", font=('Arial 12 bold')).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

opt = tk.StringVar(root)
options = ['0','1']

#Janela
root.title('Alarme | Everton Espedito')
root.geometry("600x350")
root.resizable(width=0, height=0)
root.mainloop()