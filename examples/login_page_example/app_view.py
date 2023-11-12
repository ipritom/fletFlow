import flet as ft
from fletFlow import fletFlowView

class MainAppView(fletFlowView):
    def __init__(self, page: ft.Page):
        super().__init__(page)
    
    def controls(self):
        self.logout_button = ft.ElevatedButton("Logout", on_click=self.log_out_seq)

    def layout(self):
        layout = ft.Row([
            ft.Container(ft.Column([
                self.logout_button
            ]))
        ])
        return layout


    def log_out_seq(self, e):
        self.page.client_storage.clear()
        self.page.go("/")
        self.page.update()
    
    def redirect(self):
        if self.page.client_storage.get("login"):
            return "/app"
        else:
            return "/"