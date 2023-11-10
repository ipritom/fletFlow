from abc import abstractmethod
import flet as ft

from fletFlow.views import fletFlowView


class FletFlowApp:
    """Main App Class for FletFlow"""
    def __init__(self, title=None) -> None:
        self.title = title

        if title == None:
            self.title = "fletFlow App Window"

        self.page : ft.Page = None

        self.views_map : dict(str, fletFlowView) = {}

    @abstractmethod
    def views(self, page:ft.Page):
        '''
        Register View Class objects here in this App class method

        self.register_view("<route name>", LoginView)
        '''
    
    def on_route_change_handler(self, route:ft.RouteChangeEvent):
        flow_route = route.route
        print('flow_route :', flow_route)
        # clear the last view
        self.page.views.clear()
        # constructing the view object pointed by route and initializing
        view_object: fletFlowView = self.views_map[flow_route](self.page)

        # # check redirect
        # redirect = hasattr(view_object, "redirect")
        # print('redirect', redirect)
        # if redirect:
        #     print("--- redirecting", flow_route)
        #     redirect_route = view_object.redirect()
        #     print(" --- to ", redirect_route)
        #     if redirect is not None:
        #         flow_route = redirect_route

        #     print(" --- to ", flow_route)
        #     view_object: fletFlowView = self.views_map[flow_route](self.page)

        # rendering the view on the page
        view_object.controls()
        self.page.views.append(view_object(flow_route))
        self.page.update()
    
    @abstractmethod
    def app_presentaion(self):
        '''
        App Presentation Logic under this method
        Define initial landing page
        '''
        pass

    def register_view(self, route:str=None, view_class:fletFlowView=None):
        """Register FletView object with corresponding route"""
        if route is None:
            raise TypeError("route cannot be none")

        self.views_map[route] : fletFlowView =  view_class


    def main(self, page:ft.Page):
        # assign page attribute to the class
        self.page = page
        # creating page
        self.page.title = self.title
        self.views(self.page)
        self.page.on_route_change = self.on_route_change_handler
        self.app_presentaion()
        page.update()


    def run(self):
        ft.app(target=self.main)
