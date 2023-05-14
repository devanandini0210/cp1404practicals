from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__()
        self.names =["Bob", "Mary", "Jeremy Renner", "Greg"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        main = self.root.ids.main
        for name in self.names:
            label = Label(text=name)
            main.add_widget(label)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = name


DynamicLabelsApp().run()
