import flet as ft
from fletFlow import FletFlowApp

from login_view import LoginView
from registration_view import RegisterView
from app_view import MainAppView


class App(FletFlowApp):
    def __init__(self, title=None) -> None:
        super().__init__(title)
    
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
        # if self.page.client_storage.get('login'):
        #     self.page.go("/app")
        # else:
        #     self.page.go("/")
        

    def run(self):
        # ft.app(target=main, host=host_ip, port=host_port, view=ft.WEB_BROWSER, upload_dir="uploads", assets_dir="uploads")
        ft.app(target=self.main, port=59441, view=ft.WEB_BROWSER, upload_dir="uploads", assets_dir="uploads")



app = App(title="Flet Example")
app.run()
