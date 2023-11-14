from abc import abstractmethod
import flet as ft

class fletFlowView:
    def __init__(self, page: ft.Page) -> None:
        """
        FletView Parameters
        """
        self.page = page
        self.__has_redirect_logic = False
        # check redirect
        if hasattr(self, "redirect"):
            self.__has_redirect_logic = True

    @abstractmethod
    def layout(self):
        '''
        APP GUI Layout Code under this method
        '''
        pass

    @abstractmethod
    def controls(self):
        '''
        Flet Controls which will be resued in the app dynamically
        under this method.
        '''
        pass
    
    
    def __call__(self, route):
        load_controls = self.layout()
        if isinstance(load_controls, list):
            return ft.View(route=route, controls=self.layout())
        else:
            return ft.View(route=route, controls=[self.layout()])

    def has_redirect(self):
        return self.__has_redirect_logic