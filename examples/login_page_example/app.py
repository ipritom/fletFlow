import flet as ft
from fletFlow import fletFlowApp

from login_view import LoginView
from registration_view import RegisterView
from app_view import MainAppView


class App(fletFlowApp):
    def __init__(self, title=None, debug=False) -> None:
        super().__init__(title, debug)
    
    def config_page_settings(self):
        self.page.theme_mode = ft.ThemeMode.LIGHT
        theme = ft.Theme()
        theme.page_transitions.windows = ft.PageTransitionTheme.NONE
        theme.page_transitions.linux = ft.PageTransitionTheme.NONE
        self.page.theme = theme
        

    def views(self, page:ft.Page):
        self.register_view("/", LoginView)
        self.register_view("/reg", RegisterView)
        self.register_view("/app", MainAppView)

    def app_presentaion(self):
        self.config_page_settings()
        self.page.go("/")
        
    def run(self):
        ft.app(target=self.main, view=ft.WEB_BROWSER)


app = App(title="Flet Example", debug=True)
app.run()
