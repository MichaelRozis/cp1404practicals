from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user using the name from the TextInput."""
        name = self.root.ids.input_name.text
        if name == "":
            name = "stranger"
        self.root.ids.output_label.text = "Hello " + name

    def handle_clear(self):
        """Clear the TextInput and reset the Label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"


# Run the app
BoxLayoutDemo().run()