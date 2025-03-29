from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """
    A simple Kivy application that demonstrates the use of BoxLayout
    to create a GUI where users can enter their name and receive a greeting
    or clear the input.
    """

    def build(self):
        """
        Builds the application interface by loading the KV file and setting
        the application title.

        Returns:
            The root widget of the application.
        """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """
        Handles the event when the greet button is pressed.

        Retrieves the name from the TextInput and updates the output label
        to display a greeting message. The greeting format can be adjusted
        through a template string.

        This method is triggered when the greet button is pressed.
        """
        name = self.root.ids.input_name.text
        greeting_template = "Hello {}"  # Template string for the greeting
        self.update_output_label(greeting_template.format(name))

    def handle_clear(self):
        """
        Handles the event when the clear button is pressed.

        Clears both the TextInput and the output label to reset the application
        state. This method is triggered when the clear button is pressed.
        """
        self.clear_inputs()

    def update_output_label(self, message):
        """
        Updates the output label with the specified message.

        Args:
            message (str): The message to display in the output label.
        """
        self.root.ids.output_label.text = message

    def clear_inputs(self):
        """
        Clears the TextInput and output label to reset the application state.
        """
        self.root.ids.input_name.text = ''
        self.update_output_label('')  # Clear the greeting message



# Run the application
if __name__ == "__main__":
    BoxLayoutDemo().run()
