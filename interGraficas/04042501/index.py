import flet as ft
import sqlite3

class ToDo:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.window.min_height = 650
        self.page.window.min_width = 440
        self.page.window.resizable = True
        self.page.window.always_on_top = True
        self.page.title = "Lista de Tarefas"
        self.page.bgcolor = "#4F4F4F"
        self.db_execute('CREATE TABLE IF NOT EXISTS tasks(name,status)')
        self.page.update() # para aplicar as mudanças

        self.main_page()

    def db_execute(self,query,params = []):
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query,params)
            con.commit()
            return cur.fetchall()
        
    def task_container(self):
        return ft.Container(
            height=self.page.height *0.8, #tamanho do container vai ser = 80%
            content=ft.Column(
                controls=[
                    ft.Checkbox(label="Tarefa 1",value= True)
                ]
            )
        )    
    def main_page(self):
        input_task = ft.TextField(hint_text="Digite uma Tarefa",expand=True,text_size=20,fill_color="#1C1C1C")

        input_bar= ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor="#800000")
            ]
        )  
        tabs = ft.Tabs(
            selected_index=0,
            # overlay_color= "#1C1C1C",
            label_color= "#800000", #Tab selecionada
            indicator_color = "#DC143C", # Barra de seleção
            tabs=[
                ft.Tab(text="Todos"),
                ft.Tab(text="Em andamento"),
                ft.Tab(text="Concluídos"),
            ],
        )

        tasks = self.task_container()
        self.page.add(input_bar,tabs, tasks)
        
ft.app(target= ToDo)        