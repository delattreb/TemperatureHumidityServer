"""
com_config.py v 1.0.2
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import configparser
import os.path

config_file = "config/config.ini"


def setConfig():
    config = configparser.ConfigParser()
    acquisitionDuration = 1
    # region Config
    # Version
    config['APPLICATION'] = {}
    config['APPLICATION']['name'] = 'Temp & Hum'
    config['APPLICATION']['version'] = '1.0.0'
    config['APPLICATION']['author'] = '© Bruno DELATTRE'
    config['APPLICATION']['splashduration'] = '5'
    config['APPLICATION']['refreshsensor'] = '5'

    # Acquisition
    config['ACQUISITION'] = {}
    config['ACQUISITION']['trigger'] = '10'
    
    # LOGGER
    config['LOGGER'] = {}
    config['LOGGER']['levelconsole'] = '10'  # DEBUG=10 INFO=20 WARNING=30 ERROR=40 #CRITICAL=50
    config['LOGGER']['levelfile'] = '20'
    config['LOGGER']['logfile'] = 'log'
    config['LOGGER']['logfilesize'] = '1000000'
    
    # SQLite
    config['SQLITE'] = {}
    config['SQLITE']['database'] = 'database.db'
    
    # GPIO
    config['GPIO'] = {}
    
    # DHT22
    config['GPIO']['DHT22_INTERIOR_PORT'] = '5'
    config['GPIO']['DHT22_INTERIOR_delay'] = '10'
    
    # DS18B20
    config['GPIO']['DS18B20_1'] = '/sys/bus/w1/devices/w1_bus_master1/28-0416618c01ff/w1_slave'
    config['GPIO']['DS18B20_1_delay'] = '10'
    config['GPIO']['DS18B20_1_nb'] = str(int(((acquisitionDuration * 3600) / float(config['GPIO']['DS18B20_1_delay']))))
    
    config['GPIO']['DS18B20_2'] = ''
    config['GPIO']['DS18B20_2_delay'] = '10'
    config['GPIO']['DS18B20_2_nb'] = str(int(((acquisitionDuration * 3600) / float(config['GPIO']['DS18B20_2_delay']))))
    
    # LED
    config['GPIO']['LED_ACQUISITION'] = '23'
    
    # INPUT
    config['GPIO']['INPUT_ACQUISITION'] = '27'
    
    # endregion
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, config_file)
    with open(db_path, 'w') as configfile:
        config.write(configfile)


def getConfig():
    config = configparser.RawConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, config_file)
    config.read(db_path)
    return config
