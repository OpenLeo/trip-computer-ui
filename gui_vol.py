from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

class volume:
    def __init__(self):
        self.clock = None

    def build(self):
        self.layout = Builder.load_file('gui_vol.kv')
        return self.layout

    def consume(self, item):
        if item['value']['show']:
            # Change before timeout: unschedule and redo
            if self.clock:
                self.clock.cancel()

            self.layout.opacity = 1
            self.layout.ids.volume.value = item['value']['volume']
            self.layout.ids.volumetext.text = f"{item['value']['volume']}"
            self.clock = Clock.schedule_once(self.reset, 5)

    def reset(self, dt):
        self.layout.opacity = 0
        self.clock = None
