import flet as ft

USUARIO = "admin"
CONTRASEÑA = "admin123"

def recuperar_contraseña(e):
    print("Recuperar contraseña")

def main(page: ft.Page):

    page.title = "Login"
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    txt_usuario = ft.TextField(
        width=280,
        height=40,
        hint_text="Correo electronico",
        border=ft.InputBorder.UNDERLINE,
        color="black",
        prefix_icon=ft.Icons.EMAIL
    )

    txt_contraseña = ft.TextField(
        width=280,
        height=40,
        hint_text="Contraseña",
        border=ft.InputBorder.UNDERLINE,
        color="black",
        prefix_icon=ft.Icons.KEY,
        password=True
    )

    def cerrar_dialogo(e):
        page.dialog.open = False
        page.update()

    def mostrar_pantalla_principal():
        page.clean()

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explorar"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ]
        )

        page.add(ft.Text("Bienvenido al sistema", size=30, color="white"))
        page.update()

    def login_click(e):
        usuario = txt_usuario.value
        contraseña = txt_contraseña.value

        if usuario == USUARIO and contraseña == CONTRASEÑA:
            mostrar_pantalla_principal()
        else:
            error_dialog = ft.AlertDialog(
                title=ft.Text("Error de Acceso"),
                content=ft.Text("Usuario o contraseña incorrectos."),
                actions=[
                    ft.TextButton("Entendido", on_click=cerrar_dialogo)
                ]
            )

            page.dialog = error_dialog
            error_dialog.open = True
            page.update()

    container = ft.Container(
        ft.Column(
            [
                ft.Text(
                    "Iniciar sesión",
                    width=320,
                    size=30,
                    text_align="center",
                    weight="w900",
                    color="black"
                ),

                txt_usuario,
                txt_contraseña,

                ft.TextButton(
                    "¿Olvidaste tu contraseña?",
                    on_click=recuperar_contraseña
                ),

                ft.ElevatedButton(
                    text="Iniciar",
                    width=280,
                    on_click=login_click
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        border_radius=20,
        width=320,
        height=500,
        gradient=ft.LinearGradient([
            ft.Colors.PINK_200,
            ft.Colors.PURPLE_200,
            ft.Colors.WHITE
        ])
    )

    page.add(container)

ft.app(target=main)