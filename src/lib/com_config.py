# -*- coding: utf-8 -*-
"""
com_config.py v 1.0.2
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import configparser
import os.path

config_file = "config/config.ini"


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
    
    def setconfig(self):
        acquisitionduration = 6  # In hours
        
        # region Config
        # Version
        self.config['APPLICATION'] = {}
        self.config['APPLICATION']['name'] = 'TemperatureHumidity'
        self.config['APPLICATION']['version'] = '1.0.0'
        self.config['APPLICATION']['author'] = u'\u00A9' + ' Bruno DELATTRE'
        self.config['APPLICATION']['splashduration'] = '5'
        
        # WEBServices
        self.config['WEBSERVICES'] = {}
        self.config['WEBSERVICES']['port'] = '9090'
        self.config['WEBSERVICES']['url'] = 'http://localhost:' + self.config['WEBSERVICES']['port']
        
        # Acquisition
        self.config['ACQUISITION'] = {}
        self.config['ACQUISITION']['trigger'] = '5'
        
        # LOGGER
        self.config['LOGGER'] = {}
        self.config['LOGGER']['levelconsole'] = '20'  # DEBUG=10 INFO=20 WARNING=30 ERROR=40 #CRITICAL=50
        self.config['LOGGER']['levelfile'] = '20'
        self.config['LOGGER']['logfile'] = 'log'
        self.config['LOGGER']['logfilesize'] = '1000000'
        
        # SQLite
        self.config['SQLITE'] = {}
        self.config['SQLITE']['database'] = 'database.db'
        
        # GPIO
        self.config['GPIO'] = {}
        # DHT22
        self.config['GPIO']['DHT22_INTERIOR_PORT'] = '5'
        self.config['GPIO']['DHT22_INTERIOR_delay'] = '10'
        self.config['GPIO']['DHT22_INTERIOR_nb'] = str(int(((acquisitionduration * 3600) / float(self.config['GPIO']['DHT22_INTERIOR_delay']))))
        
        # DS18B20
        self.config['GPIO']['DS18B20_1'] = '/sys/bus/w1/devices/w1_bus_master1/28-0416618c01ff/w1_slave'
        self.config['GPIO']['DS18B20_1_delay'] = '10'
        self.config['GPIO']['DS18B20_1_nb'] = str(int(((acquisitionduration * 3600) / float(self.config['GPIO']['DS18B20_1_delay']))))
        
        self.config['GPIO']['DS18B20_2'] = ''
        self.config['GPIO']['DS18B20_2_delay'] = '10'
        self.config['GPIO']['DS18B20_2_nb'] = str(int(((acquisitionduration * 3600) / float(self.config['GPIO']['DS18B20_2_delay']))))
        
        # LED
        self.config['GPIO']['LED_ACQUISITION'] = '23'
        
        # INPUT
        self.config['GPIO']['INPUT_ACQUISITION'] = '27'
        # endregion
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, config_file)
        with open(db_path, 'w') as configfile:
            self.config.write(configfile)
    
    def getconfig(self):
        self.config = configparser.RawConfigParser()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, config_file)
        self.config.read(db_path)
        return self.config
