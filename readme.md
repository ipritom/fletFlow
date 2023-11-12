# fletFlow
This is framework based on flet to write flet based software program very easily. This framework aims to seperate UI code and software logic. Transition between different views is route based which is very convenient to isolate views.

This framework mostly focused on your flet skill. You just need the understanding of the `flet`. There is nothing much to learn about `fletFlow`. Just follow the simple pattern (check tutorial section). Everything else will be done by `fletFlow`.

# Feature Highlights
* Multiple views in separate scripts
* Write your project with OOP.
* Flexible and modular; easy to use.
* Redirect views based on authetication logic.

# How to use
## Installation
Install from GitHub
```
pip install git+https://github.com/ipritom/fletFlow

```
* Should have [Git](https://git-scm.com/) installed on your system.

## Tutorial
Check an example in the `examples` directory. 
This module will help you to write flet based software with separation of concern. 

## Basic Structure 
Structuring a Flet project with fletFlow is very simple. You just have to write 2 types of class :program.
* View Class `fletFlowView`
* App Class `fletFlowApp`

### Creating a View class 

Just inherit `fletFlowView` in your View class. You can create multiple views in a single script file. Or, you can create seperate script for different views. Follow the pattern shown bellow to create a view.

```python
from fletFlow import fletFlowView

class ExampleView(fletFlowView):
    def __init__(self, page: ft.Page):
        super().__init__(page)
    
    def controls(self):
        # create flet control objects here 
        # control objects will be arranged in the layout mehtod

    def layout(self):
        # this method witll return app layout
    
    # add more methods for you app
```

The three methods (`__init__`, `controls()`, `layout()`) are responsible for creating views for your app. You can add more methods for button click functions. 

### Creating a App class

Inherit `fletFlowApp` app to create your app class. Register your views inside `views()` method. Create an object of your app class. Run your app. This is super simple!

```python
from fletFlow import fletFlowApp, fletFlowView

from views import ExampleView

class App(fletFlowApp):
    def __init__(self, title=None, debug=False):
        super().__init__(title, debug)
    
    def views(self):
        # register views here with route 
        self.register_view("/", ExampleView)
    
    def app_presentaion(self):
        # app presentation logic 
        # initialization 
        # default landing view

        
# creating app object and running the app
app = App(title="Example")
app.run()

```
For enabling debug mode:
```python
app = App(title="Example", debug=True)
```
You are running the app with `app.run()`. You can write your own `run()` method inside your app class. This method will contain `ft.app()`. 
