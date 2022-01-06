#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import serial
import random
import logging
import re
import sys
import struct
import math
import locale
from time import sleep
from datetime import datetime
from threading import Thread
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock, _default_time as time  # ok, no better way to use the same clock as kivy, hmm
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.properties import ListProperty, BooleanProperty
from kivy.config import Config

from events import events

from gui_vol import volume
from gui_messages import messages

MAX_TIME = 1/60

class RootWidget(GridLayout):
    pass

class guiApp(App):

    def build(self):
        # Events
        self.evt = events()

        # Modules
        self.modules = {
            'volume': volume(),
            'messages': messages()
        }

        # Build UI
        Builder.load_file('gui.kv')
        root = RootWidget()
        self.build_modules(root)

        # Prepare events
        Clock.schedule_interval(self.consume, 0)
        return root

    def build_modules(self, root):
        for _name, module in self.modules.items():
            print(module)
            root.ids['base'].add_widget(module.build())

    def consume(self, *args):
        while self.evt.nbEvents() and time() < (Clock.get_time() + MAX_TIME):
            item = self.evt.popEvent()

            # Modules
            if item['type'] in self.modules:
                self.modules[item['type']].consume(item)
                continue

            # Simple values
            if item['type'] in self.root.ids:
                self.root.ids[item['type']].text = item['value']
