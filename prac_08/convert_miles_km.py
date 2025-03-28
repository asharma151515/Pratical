from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION_FACTOR = 1.60934


class MilesToKilometersConverterApp(App):
    """ Kivy App for converting miles to kilometres """

    # StringProperty to automatically update the label text
    output_kilometers = StringProperty("0.0 km")

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Miles to Kilometres Converter"
        return Builder.load_file('convert_miles_km.kv')

    def calculate_kilometers(self):
        """ Calculate kilometers from miles and update the output label """
        miles = self.get_miles_input()
        kilometers = miles * MILES_TO_KM_CONVERSION_FACTOR
        self.output_kilometers = f"{kilometers:.2f} km"  # Automatically updates the label

    def increment_miles(self, change):
        """
        Increment or decrement the miles input and recalculate
        :param change: the amount to change (positive or negative)
        """
        current_miles = self.get_miles_input() + change
        self.root.ids.input_miles.text = str(current_miles)
        self.calculate_kilometers()

    def get_miles_input(self):
        """
        Retrieve and validate the miles input; return 0 if invalid
        :return: float of the input value or 0
        """
        try:
            text = self.root.ids.input_miles.text
            return float(text) if text else 0  # Return 0 for empty input
        except ValueError:
            return 0


if __name__ == '__main__':
    MilesToKilometersConverterApp().run()
