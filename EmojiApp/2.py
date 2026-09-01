import flet as ft

# Lista de emojis para aparecer no app
EMOJIS = ["🍆", "💦", "😍" ,"🍒" ,"🍑" ,"🍌" ,"👌" ,"😈" ,"😏" ,"🔥",]
# IDX controla o índice do emoji atual na lista EMOJIS
IDX = 0

# Função principal do aplicativo, recebe um objeto Page como argumento
# Page é criada pelo Flet e representa a janela do aplicativo
def main(page: ft.Page):
    # ----- Configurações da página
    # editar titulo da página 
    page.title = "EmojiApp"
    # definir alinhamento vertical da página para centralizado
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # ----MEUS ELEMENTOS {C0NTROLS}
    # size define o tamanho do elemento, nesse caso 100px
    # value define o valor inicial do elemento, nesse caso o emoji na posição 8 da lista EMOJIS
    input = ft.Text(value=EMOJIS[8], size=100)
    input2 = ft.Text(value=EMOJIS[5], size=100)
    input3 = ft.Text(value=EMOJIS[0], size=100)
    input4 = ft.Text(value=EMOJIS[4], size=100)
    input5 = ft.Text(value=EMOJIS[7], size=100)
    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[input, input2, input3, input4, input5]
    )   

    # Função é executada quando o botão de refresh é clicado
    # Atualiza os valores dos EMOJIS
    # declaradas na função main, por isso é necessário declarar como global
    def refresh_click(e):
        global IDX
        btn = e.control
        if btn.icon == ft.Icons.ARROW_RIGHT_SHARP:
            # Incremento circular
            #      * acresce 10x em 1
            #      * Se IDX > tamanho da lista EMOJIS, volta para 0
            IDX = (IDX + 1)
        else:
            IDX = (IDX - 1)
        IDX = IDX % len(EMOJIS)[IDX]
        # Incremento circular
        #      * acresce 10x em 1
        #      * Se IDX > tamanho da lista EMOJIS, volta para 0
        IDX = (IDX + 1) % len(EMOJIS)
        input.value = EMOJIS[IDX]
        input2.value = EMOJIS[(IDX + 1) % len(EMOJIS)]
        input3.value = EMOJIS[(IDX + 2) % len(EMOJIS)]
        input4.value = EMOJIS[(IDX + 3) % len(EMOJIS)]
        input5.value = EMOJIS[(IDX + 4) % len(EMOJIS)]
        # Atualiza a página para refletir as mudanças
    page.add(row)

    # Elemento de layout
    # ft.Row é um container que organiza os elementos em linha
    # alignment=ft.MainAxisAlignment.CENTER centraliza os elementos na linha
    # controls=[input, btn] define os elementos que estarão dentro do Row
    btn = ft.IconButton(ft.Icons.REFRESH, on_click=refresh_click)
    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            input,
            btn
        ]     
    )
    # adicionando os elementos na página
    # como "row" contem "input" e "btn", ambos serão exibidos na página
    # para ver ver todos os elementos criados
    page.add(row)

if __name__ == "__main__":
    # ft.run() inicia o aplicativo Flet
    # aponta para a função main que será executada quando o app iniciar
    ft.app(target=main)