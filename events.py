class singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class events(metaclass=singleton):
    events = []

    def addEvent(self, event):
        self.events.append(event)

    def nbEvents(self):
        return len(self.events)

    def popEvent(self):
        return self.events.pop(0)

