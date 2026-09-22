import flet as ft
import os

from model import Book
from database import Database

def main(page: ft.Page):
    page.title = "Book App - Lista de Livros"
    page.padding = 20
    db_path = os.path.join(
        os.environ('HOME'), 'FletProject', 'BookApp', 'src',
        'bookapp.db'
    )
    db = Database(db_path)
    # durante inserção no banco
    book = Book('Harry Potter', 'J. K. Rowling', 'A história de um jovem bruxo que descobre seus poderes e enfrenta desafios mágicos.', 29.99)
    db.insert(book)

    books_col = ft.Column(
        expand=True, 
        scroll=ft.ScrollMode.ALWAYS,
        spacing=15
    )

    # ----- LÓGICA -----
    def add_book(e):
        titulo = input_titulo.value.strip()
        autor = input_autor.value.strip()
        descricao = input_descricao.value.strip()
        preco = input_preco.value.strip()

        if titulo != "":
            # Elementos de texto do livro
            txt_titulo = ft.Text(titulo, size=25, color=ft.Colors.BLUE)
            txt_autor = ft.Text(f"Autor: {autor}")
            txt_descricao = ft.Text(descricao)
            
            # Formatação do preço
            preco_formatado = f"R$ {preco}" if preco else ""
            txt_preco = ft.Text(preco_formatado)

            # Função para excluir este livro específico
            def delete_book(e):
                books_col.controls.remove(book_card)
                page.update()

            # Botão de excluir com ícone de lixeira
            btn_delete = ft.IconButton(
                icon=ft.Icons.DELETE,
                icon_color=ft.Colors.RED,
                tooltip="Excluir livro",
                on_click=delete_book
            )

            # Coluna à esquerda: Título, Autor e Descrição um embaixo do outro
            info_column = ft.Column(
                controls=[txt_titulo, txt_autor, txt_descricao],
                expand=True,
                spacing=3
            )

            # Linha principal do item: Coluna de informações + Preço + Botão de exclusão
            book_card = ft.Row(
                controls=[info_column, txt_preco, btn_delete],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
            
            # Insere no início da lista (aparece logo abaixo do formulário)
            books_col.controls.insert(0, book_card)
            
            # Limpa os campos após adicionar
            input_titulo.value = ""
            input_autor.value = ""
            input_descricao.value = ""
            input_preco.value = ""
            input_titulo.focus()
            page.update()

    # Campos de texto do formulário
    input_titulo = ft.TextField(
        label="Título do Livro",
        on_submit=add_book
    )

    input_autor = ft.TextField(
        label="Autor",
        on_submit=add_book
    )

    input_descricao = ft.TextField(
        label="Descrição",
        on_submit=add_book
    )

    input_preco = ft.TextField(
        label="Preço",
        on_submit=add_book
    )

    # Botão de adicionar em formato de "bolinha" circular
    btn_add = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE,
        tooltip="Adicionar livro",
        on_click=add_book
    )

    # Coluna contendo os quatro campos empilhados no formulário
    inputs_column = ft.Column(
        controls=[input_titulo, input_autor, input_descricao, input_preco],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    )

    # Linha principal ("div") do formulário
    form_row = ft.Row(
        controls=[inputs_column, btn_add],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    # ----- MONTAGEM DA INTERFACE -----
    page.add(
        form_row,
        ft.Divider(),
        books_col
    )

if __name__ == "__main__":
    ft.run(main)