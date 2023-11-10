import flet as ft
from fletFlow import fletFlowView

class RegisterView(fletFlowView):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    def register_new_button_click(self, e):
        pass

    
    def login_page_button_click(self, e):
        self.page.go("/")

    def controls(self):
        # declare all the controls related to this view
        self.full_name = ft.TextField(label="Full Name", visible=False, autofocus=True)
        self.user_name = ft.TextField(label="Username", visible=False, autofocus=True)
        self.employee_id = ft.TextField(label="Employee ID", visible=False, autofocus=True)
        self.viber_token_input = ft.TextField(label="Viber Token", visible=True, autofocus=True)
        self.register_new_button =  ft.ElevatedButton("Authenticate", visible=True, data="NONE")
        self.login_page_button = ft.ElevatedButton("Login", visible=True, on_click=self.login_page_button_click)
        self.warning_text = ft.Text("", size=25, color=ft.colors.RED)

    def layout(self):
        # write the layout code under this method
        layout = ft.Row([
            ft.Container(content=ft.Column([self.viber_token_input, 
                                      self.full_name, self.user_name, 
                                      self.employee_id,
                                      ft.Text("Say 'Hi' to WalBot in Viber to get the authentication code.", color=ft.colors.BLUE_900, selectable=True),
                                      ft.Row([self.register_new_button, self.login_page_button]),
                                      self.warning_text],
                                      width=500),
                                      padding=200,  alignment=ft.alignment.top_center,
                                      expand=True, bgcolor=ft.colors.BLUE_GREY_100, border_radius=20)
                        ], 
                        expand=True)

        return layout
                
        