import flet as ft

def main(page: ft.Page):
    page.title = "Lista de pessoas"
    page.padding = 20

    tasks_col = ft.Column(
        expand=True, 
        scroll=ft.ScrollMode.ALWAYS
    )

    # ----- LÓGICA -----
    def add_person(e):
        nome = input_txt.value.strip()
        idade = input_idade.value.strip()
        email = input_email.value.strip()

        if nome != "":
            # Elementos de texto individuais para cada pessoa
            txt_label = ft.Text(nome, expand=True)
            txt_idade = ft.Text(idade, expand=True)
            txt_email = ft.Text(email, expand=True)

            # Função para excluir esta linha específica
            def delete_person(e):
                tasks_col.controls.remove(task_row)
                page.update()

            # Botão de excluir com ícone de lixeira para a linha
            btn_delete = ft.IconButton(
                icon=ft.Icon(icon=ft.Icons.DELETE, color=ft.Colors.RED),
                tooltip="Excluir pessoa",
                on_click=delete_person
            )

            # Agrupa os elementos em uma linha (sem o checkbox)
            task_row = ft.Row(
                controls=[txt_label, txt_idade, txt_email, btn_delete],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
            
            # Insere no início da lista (aparece logo abaixo do formulário)
            tasks_col.controls.insert(0, task_row)
            
            # Limpa os campos após adicionar
            input_txt.value = ""
            input_idade.value = ""
            input_email.value = ""
            input_txt.focus()
            page.update()

    # Campos de texto com suporte à tecla ENTER
    input_txt = ft.TextField(
        hint_text="Nome",
        expand=True,
        on_submit=add_person
    )

    input_idade = ft.TextField(
        hint_text="Idade",
        expand=True,
        on_submit=add_person
    )

    input_email = ft.TextField(
        hint_text="Email",
        expand=True,
        on_submit=add_person
    )

    # Botão para adicionar 
    btn_add = ft.ElevatedButton(
        content="Adicionar",
        on_click=add_person
    )

    # ----- MONTAGEM DA INTERFACE -----
    page.add(
        ft.Row([input_txt, input_idade, input_email]),
        btn_add,
        ft.Divider(),
        tasks_col
    )

if __name__ == "__main__":
    ft.run(main)
