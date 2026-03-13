import flet as ft

def recuperar_contraseña(e):
    print("Recuperar contraseña")

container = ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                "Iniciar sesión",
                width=320,
                size=30,
                text_align="center",
                weight="w900",
                color="black"
            ),
            padding=ft.Padding.only(top=20, bottom=20)
        ),

        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Correo electronico",
                border=ft.InputBorder.UNDERLINE,
                color="black",
                prefix_icon=ft.Icons.EMAIL
            ),
            padding=ft.Padding.only(top=20, bottom=20)
        ),

        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Contraseña",
                border=ft.InputBorder.UNDERLINE,
                color="black",
                prefix_icon=ft.Icons.KEY,
                password=True
            ),
            padding=ft.Padding.only(top=20, bottom=10)
        ),

        ft.TextButton(
            "¿Olvidaste tu contraseña?",
            on_click=recuperar_contraseña
        ),

        ft.Container(
            ft.Button(
                content=ft.Text("Iniciar"),
                width=280
            ),
            padding=ft.Padding.only(top=20, bottom=20)
        )
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

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(container)

ft.app(target=main)