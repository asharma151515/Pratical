from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class MilesToKmConverter(App):
    conversion_result = StringProperty('')

    def build(self):
        self.title = "Convert Miles to Kilometers "
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_km(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * 1.60934
            self.conversion_result = f"{kilometers:.2f} km"
        except ValueError:
            self.conversion_result = "Invalid input!"

    def clear_input_and_result(self):
        self.root.ids.input_miles.text = ''
        self.conversion_result = ''

    def increment_miles(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            miles += 1
            self.root.ids.input_miles.text = str(miles)
            self.convert_miles_to_km()
        except ValueError:
            self.root.ids.input_miles.text = '1'
            self.convert_miles_to_km()

    def decrement_miles(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            miles -= 1
            self.root.ids.input_miles.text = str(miles)
            self.convert_miles_to_km()
        except ValueError:
            self.root.ids.input_miles.text = '0'
            self.convert_miles_to_km()

MilesToKmConverter().run()