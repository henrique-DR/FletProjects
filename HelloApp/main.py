import flet as ft

def main(page: ft.Page):
    # muda o título da janela no app e do app no mobile
    page.title = 'HelloApp' 
    # alinha verticalmente os elementos da página no centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # cria um componente visual de texto
    text = ft.Text(value='Hello, World!',)
    text_align = ft.TextAlign.CENTER,
    # metodo add adiciona elementos (controls) dentro da página
    #para ser mostrado na tela
    page.add(text)


if __name__ == '__main__':
    # ft.app cria o objeto: page = page()
    # o objeto page é enviado para a função target {main}
    # para ser preenchido
    ft.app(target=main)
    