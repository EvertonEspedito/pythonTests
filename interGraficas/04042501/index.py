import flet as ft

class ToDo:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.window.height = 650
        self.page.window.width = 440
        self.page.window.resizable = False
        self.page.window.always_on_top = True
        self.page.title = "Lista de Tarefas"
        self.page.bgcolor = "#4F4F4F"
        self.page.update() # para aplicar as mudanças

        self.main_page()
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

        self.page.add(input_bar,tabs)
        
ft.app(target= ToDo)        