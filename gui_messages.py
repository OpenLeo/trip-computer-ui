from kivy.app import App
from kivy.lang import Builder

class messages:
    def build(self):
        self.layout = Builder.load_file('gui_messages.kv')
        return self.layout

    def consume(self, item):
        if item['value']['show'] == True:
            self.layout.opacity = 1
            self.layout.ids.message.text = item['value']['text']
        else:
            self.layout.opacity = 0
