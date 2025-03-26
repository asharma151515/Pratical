from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """
    A simple Kivy application that demonstrates the use of BoxLayout.
    """

    def build(self):
        """
        Loads the kv file and sets the title for the app.

        Returns:
            The root widget defined in the kv file.
        """
        self.title = "Box Layout Demo"  # Set the title of the app
        self.root = Builder.load_file('box_layout.kv')  # Load the kv file
        return self.root  # Return the root widget


# Run the application
if __name__ == "__main__":
    BoxLayoutDemo().run()
