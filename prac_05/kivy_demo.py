from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button


class KivyDemoApp(App):
    """Kivy program to demo some basic interactive functionality."""
    status_text = StringProperty("Hello. Click the buttons :)")

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        self.counter = 0
        self.names = ["Lindsay", "Osmond", "Paul"]  # Dynamic list of names

    def build(self):
        """Construct the dynamic widgets."""
        self.title = "Hello World!"
        self.root = Builder.load_file('kivy_layout.kv')  # Load KV layout

        # Create buttons dynamically from the names list
        for name in self.names:
            button = Button(text=name)  # Create button for each name
            button.bind(on_press=self.handle_name_button)  # Bind press event
            self.root.ids.names_box.add_widget(button)  # Add to layout

        return self.root

    def handle_name_button(self, instance):
        """Handle presses on the name button to greet people."""
        print("Hello", instance.text)

    def handle_press(self, amount):
        """Handle presses on the increment/decrement buttons."""
        self.counter += amount
        self.status_text = f"The count is: {self.counter}"  # Update the status text


# Create an instance of the KivyDemoApp class and start the App running
if __name__ == '__main__':
    KivyDemoApp().run()
