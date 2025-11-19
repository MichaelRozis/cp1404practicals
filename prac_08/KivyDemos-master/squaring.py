"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Michael Rozis, IT@JCU
Started 17/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Michael Rozis'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)  # Wider window for horizontal layout
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation when button is pressed."""
        try:
            value = float(self.root.ids.input_number.text)
            result = value ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


SquareNumberApp().run()