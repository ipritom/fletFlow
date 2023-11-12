import flet as ft
from fletFlow import fletFlowView


class LightView(fletFlowView):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)


    def to_dark_page(self, e):
        self.page.theme_mode = "dark"
        self.page.update()
        self.page.go("/dark")

    def controls(self):
        self.dark_btn = ft.ElevatedButton("DARK", on_click=self.to_dark_page)

    def layout(self):
        lout = ft.Row(
                [
                    ft.Container(
                    content= self.dark_btn,
                    alignment=ft.alignment.center,
                    expand=True
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )

        return lout