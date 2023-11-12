from abc import abstractmethod
import datetime

import flet as ft
from fletFlow.views import fletFlowView


class fletFlowApp:
    """Main App Class for FletFlow"""
    def __init__(self, title=None, debug=False) -> None:
        self.title = title

        if title == None:
            self.title = "fletFlow App Window"

        self.page : ft.Page = None
        self.views_map : dict(str, fletFlowView) = {}
        self.debug = debug

        # trace the change of route while handling change [pre, new(user asked), redirected, actual(set to page)]
        self.__trace_change_route = {
            "pre" : None,
            "new" : None,
            "redirected" : None,
            "actual" : None,
        }


    @abstractmethod
    def views(self, page:ft.Page):
        '''
        Register View Class objects here in this App class method

        self.register_view("<route name>", LoginView)
        '''
    
    @abstractmethod
    def app_presentaion(self):
        '''
        App Presentation Logic under this method
        Define initial landing page
        '''
        pass


    def __is_valid_route(self, route:str):
        """Check if the route is registered"""
        return route in self.views_map

    def __debug(self, msg:str, param:any):
        if self.debug:
            print(f"fletFlow : {datetime.datetime.now()} | {msg} | {param}")

    def __reset_trace_change_route(self):
        self.__trace_change_route = {
            "pre" : None,
            "new" : None,
            "redirected" : None,
            "actual" : None,
        }

    def on_route_change_handler(self, route:ft.RouteChangeEvent):
        """Handle page route changing"""
        self.__reset_trace_change_route()
        self.__trace_change_route["pre"] = self.page.views[-1].route
        # validate route
        if not self.__is_valid_route(route.route):
            return

        flow_route = route.route
        self.__trace_change_route["new"] = flow_route
        # constructing the view object pointed by route
        view_object: fletFlowView = self.views_map[flow_route](self.page)

        # check redirect
        if view_object.has_redirect():
            redirect_route = view_object.redirect()
            if redirect_route is not None:
                flow_route = redirect_route
                self.__trace_change_route["redirected"] = flow_route
            # re-constructing the view object pointed by redirect route
            view_object: fletFlowView = self.views_map[flow_route](self.page)
    
        self.__trace_change_route["actual"] = self.page.route
        self.__debug("trace change of route", self.__trace_change_route)

        # avoiding redundant trigger (pre==actual redirected route and page.route is same)
        if self.__trace_change_route["pre"]==self.__trace_change_route["actual"]:
            self.__debug("bypassing redundant view change", "")
            return

        # clear the last view
        self.page.views.clear()
        # rendering the new view on the page
        self.__debug("calling view", view_object.__class__.__name__)
        view_object.controls()
        self.page.views.append(view_object(flow_route))
        self.page.route = flow_route # NOTE: cause redundant trigger on change handler
        self.page.update()

    def register_view(self, route:str=None, view_class:fletFlowView=None):
        """Register FletView object with corresponding route"""
        if route is None:
            raise TypeError("route cannot be none")

        self.views_map[route] : fletFlowView =  view_class


    def main(self, page:ft.Page):
        """
        Main method to run flet Window
        Flet flow automatically handle this function
        """
        self.page = page
        self.page.title = self.title
        self.page.on_route_change = self.on_route_change_handler
        self.views(self.page)
        self.app_presentaion()
        page.update()

    def run(self):
        """Method for running the app"""
        ft.app(target=self.main)
