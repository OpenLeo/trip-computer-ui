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
import can
from time import sleep
from datetime import datetime
from threading import Thread

from events import events
import canmsg

class canReader():
    def __init__(self):
        self.bus = can.Bus(channel='can0', interface='socketcan', bitrate=125000)
        self.evt = events()

    def start(self):
        while True:
            recvd = self.bus.recv(1.0)
            if not recvd:
                continue

            # Handlers
            if recvd.arbitration_id in canmsg.frames:
                canmsg.frames[recvd.arbitration_id](recvd.data)

    def run(self):
        Thread(target=self.start).start()
