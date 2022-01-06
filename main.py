#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
#from kivy.config import Config

from canbus import canReader
from gui import guiApp

if __name__ == '__main__':
    #locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

    # Run CAN
    canReader().run()

    # ...
    #Config.set('graphics', 'width', '1024')
    #Config.set('graphics', 'height', '600')
    #Config.set('graphics', 'borderless', '1')

    # Run GUI
    gui = guiApp()
    gui.run()
