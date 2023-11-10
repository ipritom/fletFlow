from abc import abstractmethod
import flet as ft

class fletFlowView:
    def __init__(self, page: ft.Page) -> None:
        """
        FletView Parameters
        """
        self.page = page

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
    
    def __call__(self, route, verbose=True):
        if verbose:
            print("--- called", self.__class__.__name__)
            
        return ft.View(route=route, controls=[self.layout()])

