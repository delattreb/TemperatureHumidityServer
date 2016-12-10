"""
lcd.py v1.0.0
Auteur: Bruno DELATTRE
Date : 13/11/2016
"""

import sqlite3
import time

from lib import com_config, com_dht22, com_logger, com_ssd1306


class LCD:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        self.lcd = com_ssd1306.SSD1306()
    
    def displayoff(self):
        self.lcd.offscreen()
    
    def splash(self, duration):
        self.lcd.clear()
        self.lcd.rectangle(0, 0, self.lcd.width_max - 1, self.lcd.height_max - 1)
        self.lcd.text(4, 1, self.config['APPLICATION']['name'], 1)
        self.lcd.text(4, 17, self.config['APPLICATION']['version'], 1)
        self.lcd.text(4, 49, self.config['APPLICATION']['author'], 0)
        
        self.lcd.display()
        time.sleep(duration)
    
    def displaysensor(self):
        connection = sqlite3.Connection(self.config['SQLITE']['database'])
        cursor = connection.cursor()
        
        self.lcd.clear()
        # DHT22
        dht22 = com_dht22.DHT22(int(self.config['GPIO']['DHT22_INTERIOR_PORT']), 'DHT22')
        dht22.set(connection, cursor, False)
        self.lcd.text(1, 1, 'Temp: ' + str(dht22.temperature()) + '°C', 2)
        self.lcd.text(1, 1, 'Hum: ' + str(dht22.humidity()) + '%', 2)
        
        # DS18B20
        # ds18b20 = com_ds18b20.DS18B20()
        # self.lcd.text(1, 11, 'DS18B20 Int: ' + str(ds18b20.read('DS18B20 Interior', self.config['GPIO']['DS18B20_1'], connection, cursor, False)) + '°C', 0)
        
        self.lcd.display()
        time.sleep(int(self.config['APPLICATION']['refreshsensor']))
    
    def displaystartacquisition(self):
        logger = com_logger.Logger()
        cpt = int(self.config['ACQUISITION']['trigger'])
        for i in range(cpt):
            self.lcd.clear()
            self.lcd.text(36, 5, '- START -', 1)
            self.lcd.text(55, 35, str(int(self.config['ACQUISITION']['trigger']) - i), 2)
            self.lcd.display()
            time.sleep(1)
            logger.debug('Start in: ' + str(int(self.config['ACQUISITION']['trigger']) - i))
