"""
lcd.py v1.0.0
Auteur: Bruno DELATTRE
Date : 13/11/2016
"""

import sqlite3
import time

from lib import com_config, com_dht22, com_ds18b20, com_gps, com_logger, com_network, com_ssd1306


class LCD:
    def __init__(self):
        self.config = com_config.getConfig()
        self.lcd = com_ssd1306.SSD1306()
        self.network = com_network.NETWORK()
        self.gps = com_gps.GPS()
    
    def displayOff(self):
        self.lcd.offscreen()
    
    def splash(self, duration):
        self.lcd.clear()
        self.lcd.rectangle(0, 0, self.lcd.width_max - 1, self.lcd.height_max - 1)
        self.lcd.text(4, 1, self.config['APPLICATION']['name'], 2)
        self.lcd.text(4, 17, self.config['APPLICATION']['version'], 1)
        self.lcd.text(4, 49, self.config['APPLICATION']['author'], 0)
        
        self.lcd.display()
        time.sleep(duration)
    
    def displatSensor(self):
        config = com_config.getConfig()
        connection = sqlite3.Connection(config['SQLITE']['database'])
        cursor = connection.cursor()
        
        self.lcd.clear()
        # DHT22
        dht22 = com_dht22.DHT22(int(self.config['GPIO']['DHT22_INTERIOR_PORT']), 'DHT22')
        dht22.set(connection, cursor, False)
        self.lcd.text(1, 1, 'DHT22: ' + str(dht22.temperature()) + '°C', 0)
        self.lcd.text(85, 1, str(dht22.humidity()) + '%', 0)
        
        # DS18B20
        ds18b20 = com_ds18b20.DS18B20()
        self.lcd.text(1, 11, 'DS18B20 Int: ' + str(ds18b20.read('DS18B20 Interior', self.config['GPIO']['DS18B20_1'], connection, cursor, False)) + '°C', 0)
        
        self.lcd.display()
        time.sleep(int(config['APPLICATION']['refreshsensor']))
    
    def displayStartAcquisition(self):
        logger = com_logger.Logger()
        cpt = int(self.config['ACQUISITION']['trigger'])
        for i in range(cpt):
            self.lcd.clear()
            self.lcd.text(36, 5, '- START -', 1)
            self.lcd.text(55, 35, str(int(self.config['ACQUISITION']['trigger']) - i), 2)
            self.lcd.display()
            time.sleep(1)
            logger.debug('Start in: ' + str(int(self.config['ACQUISITION']['trigger']) - i))
