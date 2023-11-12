import flet as ft
from fletFlow import FletFlowApp, fletFlowView

from dark_page import DarkView
from light_page import LightView


class App(FletFlowApp):
    def __init__(self, title=None, debug=False):
        super().__init__(title, debug)
        
    def config_page_settings(self):
        self.page.theme_mode = ft.ThemeMode.LIGHT
        theme = ft.Theme()
        theme.page_transitions.windows = ft.PageTransitionTheme.NONE
        theme.page_transitions.linux = ft.PageTransitionTheme.NONE
        self.page.theme = theme

    def views(self, page:ft.Page):
        self.register_view("/dark", DarkView)
        self.register_view("/light", LightView)
      
    def app_presentaion(self):
        self.config_page_settings()
        self.page.go("/light")


# creating app object and running the app
app = App()
app.run()