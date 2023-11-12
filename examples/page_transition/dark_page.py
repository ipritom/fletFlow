import flet as ft
from fletFlow import fletFlowView

class DarkView(fletFlowView):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    def to_light_page(self, e):
        self.page.theme_mode = "light"
        self.page.update()
        self.page.go("/light")


    def controls(self):
        self.light_btn = ft.ElevatedButton("LIGHT", on_click=self.to_light_page)
    
    def layout(self):
        lout = ft.Row(
                [
                    ft.Container(
                    content= self.light_btn,
                    alignment=ft.alignment.center, 
                    expand=True
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )

        return lout
        