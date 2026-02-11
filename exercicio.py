import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(ft.Text("E quem disse que isso é problema meu!"))

    page.add(
        ft.Text(
            "Olá, meu nome é Homi Aranha!"
        ),
        ft.Image(
            src="images/aranha2.jpg",
            height=200
        ),
        ft.Button(
            content="Clique aqui",
            on_click=mostrar_mensagem
        )
    )
ft.app(main)