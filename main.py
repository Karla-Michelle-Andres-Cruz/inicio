import flet as ft

container = ft.Container(
    ft.Column([
        ft.Container(
            ft.text(
                
            )
        )
    ],
    alignment=ft.MainAxisAlignment.SPACE_EVENLY
    ),
    
    border_radius= 20,
    width= 320,
    height=500,
    gradient= ft.LinearGradient([
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