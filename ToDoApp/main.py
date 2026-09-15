import flet as ft

def main(page: ft.Page):
    page.title = "Minha Lista de Tarefas"
    page.padding = 20

    tasks_col = ft.Column(
        expand=True, 
        scroll=ft.ScrollMode.ALWAYS
    )

    # ----- LÓGICA -----
    def add_task(e):
        texto = input_txt.value.strip()
        
        if texto != "":
            # Elemento de texto independente
            txt_label = ft.Text(texto, expand=True)

            # Função para alternar o risco no texto
            def toggle_task(e):
                txt_label.style = ft.TextStyle(
                    decoration=ft.TextDecoration.LINE_THROUGH if chk.value else ft.TextDecoration.NONE
                )
                page.update()

            # Checkbox sem texto embutido
            chk = ft.Checkbox(on_change=toggle_task)

            # Função para deletar a tarefa
            def delete_task(e):
                tasks_col.controls.remove(task_row)
                page.update()

            # Uso correto das constantes com maiúscula: ft.Icons e ft.Colors
            btn_deletar = ft.IconButton(
                icon=ft.Icons.DELETE_OUTLINE,
                icon_color=ft.Colors.RED_400,
                tooltip="Deletar tarefa",
                on_click=delete_task
            )

            # Agrupa o checkbox, o texto e o botão de deletar
            task_row = ft.Row(
                controls=[chk, txt_label, btn_deletar],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
            
            tasks_col.controls.append(task_row)
            input_txt.value = ""
            input_txt.focus()
            page.update()

    # Campo de texto com suporte à tecla ENTER
    input_txt = ft.TextField(
        hint_text="O que você precisa fazer?",
        expand=True,
        on_submit=add_task
    )

    input_btn = ft.IconButton(
        icon=ft.Icons.ADD, 
        on_click=add_task
    )

    # ----- MONTAGEM DA INTERFACE -----
    page.add(
        ft.Row([input_txt, input_btn]),
        tasks_col
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)