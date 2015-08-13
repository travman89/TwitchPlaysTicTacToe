#!/usr/bin/env python
# created by Aidan Thomson
from sys import exit
from config.config import config
import lib.bot as bot

try:
    bot.Bot().run()
except KeyboardInterrupt:
    exit()