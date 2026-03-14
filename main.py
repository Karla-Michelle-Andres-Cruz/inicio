import flet as ft

USUARIO = "admin"
CONTRASEÑA = "admin123"

def main(page: ft.Page):

    page.title = "Inicio de Sesión"
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    mensaje_recuperacion = ft.Text(
        "",
        size=12,
        color="white",
        text_align="center",
    )

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.Colors.BLACK,
        height=50,
        content=ft.Row(
            [mensaje_recuperacion],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


    def recuperar_contraseña(e):
        mensaje_recuperacion.value = "Hemos enviado los pasos para recuperar tu contraseña a tu correo electrónico."
        page.update()

    txt_usuario = ft.TextField(
        width=280,
        height=40,
        hint_text="Correo electronico",
        hint_style=ft.TextStyle(color="black"),
        border=ft.InputBorder.UNDERLINE,
        color="black",
        prefix_icon=ft.Icons.EMAIL,
        prefix_style=ft.TextStyle(color="black")
    )

    txt_contraseña = ft.TextField(
        width=280,
        height=40,
        hint_text="Contraseña",
        hint_style=ft.TextStyle(color="black"),
        border=ft.InputBorder.UNDERLINE,
        color="black",
        prefix_icon=ft.Icons.KEY,
        prefix_style=ft.TextStyle(color="black"),
        password=True
    )

    def mostrar_contraseña(e):
        txt_contraseña.password = not txt_contraseña.password

        if txt_contraseña.password:
            txt_contraseña.suffix_icon = ft.IconButton(
                icon=ft.Icons.VISIBILITY,
                on_click=mostrar_contraseña
            )
        else:
            txt_contraseña.suffix_icon = ft.IconButton(
                icon=ft.Icons.VISIBILITY_OFF,
                on_click=mostrar_contraseña
            )

        page.update()

    txt_contraseña.suffix_icon = ft.IconButton(
        icon=ft.Icons.VISIBILITY,
        on_click=mostrar_contraseña
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

        page.add(
            ft.Text("Bienvenido a la pagina principal", size=30, color="black")
        )

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

    txt_usuario.on_submit = login_click
    txt_contraseña.on_submit = login_click

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

                ft.Button(
                    content=ft.Text("Iniciar"),
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
            ft.Colors.PINK_200
        ])
    )

    page.add(
        container
    )

ft.app(target=main)