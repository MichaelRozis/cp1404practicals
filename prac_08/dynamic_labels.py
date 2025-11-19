"""
CP1404 Practical
Dynamic Labels
"""

from kivy.app import App
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that creates labels from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        self.title = "Dynamic Labels"
        self.create_labels()
        return self.root  # root comes from dynamiclabels.kv

    def create_labels(self):
        for name in self.names:
            label = Label(text=name, font_size=48, color=(1, 1, 0, 1))
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()