import flet as ft
from fletFlow import fletFlowView

class LoginView(fletFlowView):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        
    def controls(self):
        # declare all the controls related to this view
        self.user_name = ft.TextField(label="Username", autofocus=True)
        self.entry_code = ft.TextField(label="Entry Code", visible=False, keyboard_type="number", max_length=5)
        self.login_button = ft.ElevatedButton("Submit", on_click=self.login_button_click)
        # self.register_page_button = ft.TextButton("Register",on_click=lambda e: registration_page())
        self.register_page_button = ft.TextButton("Register", on_click=self.register_page_button_click)
        self.warning_text = ft.Text("", size=25, color=ft.colors.RED)
 
    def layout(self):
        lout = ft.Row([
                    ft.Container(content=ft.Column([
                                            ft.Text("Flet App Login", size=40,weight=ft.FontWeight.W_600, italic=True),
                                            self.user_name,
                                            self.entry_code,
                                            ft.Row([self.login_button]),
                                             ft.Row([
                                                ft.Text("No Account?"), self.register_page_button,
                                                ]),
                                             self.warning_text
                                                ],
                                             width=500),
                                      padding=200,  alignment=ft.alignment.top_center,
                                      expand=True, bgcolor=ft.colors.DEEP_PURPLE_100, border_radius=20)
                    ],
                expand=True)

        return lout

    def redirect(self):
        if self.page.client_storage.get("login")==True:
            return "/app"
        else:
            return "/"

    def login_button_click(self, e):
        if self.login_button.data == "USER_SET":
            self.page.client_storage.set("login", True)
            self.page.go("/app")

        if len(self.user_name.value) == 0:
            self.warning_text.value = "please enter a valid username"
        else:
            self.user_name.visible = False
            self.entry_code.visible = True
            self.warning_text.value = ""
            self.login_button.data = "USER_SET"

        self.page.update()
    
    def register_page_button_click(self, e):
        self.page.go("/reg")