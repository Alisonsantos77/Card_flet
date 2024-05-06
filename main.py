import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK

    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),

        content=ft.Image(
            src='huggy.png',
            scale=ft.Scale(scale=1.6),
        )
    )

    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='LEVEL 4', color=ft.colors.PURPLE_500),
                ft.Text(value='Huggy',
                        color=ft.colors.PURPLE_900,
                        weight=ft.FontWeight.BOLD,
                        size=40),
                ft.Text(value='Huggy Wuggy, o monstro azul de sorriso macabro e dentes afiados. Sua lenda arrepiante '
                              'ecoa pelos corredores.',
                        color=ft.colors.PURPLE_200,
                        text_align=ft.TextAlign.CENTER,
                        )
            ]
        )
    )

    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.PURPLE_900,
        padding=ft.padding.symmetric(20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=1,
                    controls=[
                        ft.Text(value='20',
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE),
                        ft.Text(value='DEFESA', color=ft.colors.WHITE)
                    ]
                ),
                ft.VerticalDivider(opacity=0.2, color=ft.colors.WHITE),
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=1,
                    controls=[
                        ft.Text(value='16',
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE),
                        ft.Text(value='VELOCIDADE', color=ft.colors.WHITE)
                    ]
                ),
                ft.VerticalDivider(opacity=0.2, color=ft.colors.WHITE),
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=1,
                    controls=[
                        ft.Text(value='150',
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE),
                        ft.Text(value='DANO', color=ft.colors.WHITE)
                    ]
                )
            ]
        )
    )

    layout = ft.Container(
        height=700,
        width=400,
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.PURPLE_900),
        clip_behavior=ft.ClipBehavior.NONE,

        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills

            ]
        )
    )
    page.add(layout)


ft.app(target=main)
