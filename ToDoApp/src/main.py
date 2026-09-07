import flet as ft

def main(page: ft.Page):
    # Configurações básicas da página
    page.title = "Minha Lista de Tarefas"
    page.padding = 20

    # usuário digita o nome da tarefa
    input_txt = ft.TextField(
        hint_text="O que você precisa fazer?",
        expand=True  # Faz o campo ocupar todo o espaço disponível na linha
    )

    # onde as tarefas adicionadas vão aparecer
    tasks_col = ft.Column(
        expand=True, 
        scroll=ft.ScrollMode.ALWAYS  # Cria barra de rolagem se a lista ficar grande
    )

    # ----- LOGICA -----
    def add_task(e):
        texto = input_txt.value.strip()  # Pega o texto e remove espaços extras
        
        if texto != "":
            # 1. tarefa e checkbox
            nova_tarefa = ft.Checkbox(label=texto)
            
            # 2. Checkbox dentro da coluna de tarefas
            tasks_col.controls.append(nova_tarefa)
            
            # 3. limpa o campo de input para a próxima tarefa
            input_txt.value = ""
            
            # 4. Atualiza a tela no navegador para exibir a mudança
            page.update()

    # funcao add 
    input_btn = ft.IconButton(
        icon=ft.Icons.ADD, 
        on_click=add_task
    )

    # ----- MONTAGEM DA INTERFACE -----
    # Adiciona os elementos na tela
    page.add(
        ft.Row([input_txt, input_btn]),
        tasks_col
    )

# Executa o aplicativo
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)