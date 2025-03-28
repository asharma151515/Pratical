from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout  # Using GridLayout for better layout
from kivy.uix.label import Label

class MainLayout(GridLayout):
    def __init__(self, names=None, **kwargs):
        super().__init__(cols=2, **kwargs) # Set cols for GridLayout
        if names is None:
            names = ["Alice Smith", "Bob Brown", "Cat Cyan", "Oren Ochre"]
        elif not isinstance(names, list):
            print("Error: names must be a list.")
            names = [] #Handle non-list input gracefully
        elif not all(isinstance(name, str) for name in names):
            print("Error: names list must contain only strings.")
            names = [] #Handle invalid input gracefully

        self.names = names
        self.create_labels()

    def create_labels(self):
        for name in self.names:
            label = Label(text=name)
            self.add_widget(label)

class DynamicLabelsApp(App):
    def build(self):
        return MainLayout(names=["Alice Smith", "Bob Brown", "Cat Cyan", "Oren Ochre"])

if __name__ == '__main__':
    DynamicLabelsApp().run()