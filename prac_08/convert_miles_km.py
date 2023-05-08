from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Devanandini Chakravarti'


class MilesConverterApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            conversion_value = 1.609
            result = float(value) * conversion_value
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_increment(self, value, incrementing_value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) + incrementing_value
            self.root.ids.input_number.text = str(result)
        except ValueError:
            error = 0.0
            result = error + incrementing_value
            self.root.ids.input_number.text = str(result)


MilesConverterApp().run()
