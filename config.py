#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("6174366732:AAFGVJvkbNin_7E6EzDSReDVmmhIsoxHFk8")
    # The Telegram API things
    API_ID = int(os.environ.get("8130624"))
    API_HASH = os.environ.get("67a71560b00a31ffa692c67428f06d38")
    AUTH_USERS = os.environ.get("2018633153")

