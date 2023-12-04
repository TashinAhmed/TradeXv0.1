#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sun May 20 13:39:06 2018
@author: Tashin
"""
import configparser
from oandapyV20 import API

class Connection:
    config = {}
    API = None

    def __init__(self):
        # Load config
        config = configparser.ConfigParser()
        config.read('config.ini')
        mode = config['ENV']['MODE']
        Connection.config = config[mode]
        
        # Load API
        environment = Connection.config['TYPE']
        access_token = Connection.config['AUTH_TOKEN']
        Connection.API = API(access_token, environment)
