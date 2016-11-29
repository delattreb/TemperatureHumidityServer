"""
thread_acquisition_dht11.py v1.0.0
Auteur: Bruno DELATTRE
Date : 17/09/2016
"""

import sqlite3
import threading
import time

from lib import com_config, com_dht22, com_logger, com_ssd1306


class ThreadAcquisitionDHT22(threading.Thread):
    def __init__(self, name, lock, port, delay):
        super().__init__()
        
        self.name = name
        self.port = port
        self.delay = delay
        self.lock = lock
    
    def run(self):
        logger = com_logger.Logger('DHT22:' + self.name)
        logger.info('Start')
        self.getTempHum(self.delay)
        logger.info('Stop')
    
    def getTempHum(self, delay):
        instance = com_dht22.DHT22(self.port, self.name)
        while True:
            self.lock.acquire()
            
            config = com_config.getConfig()
            connection = sqlite3.Connection(config['SQLITE']['database'])
            cursor = connection.cursor()
            
            instance.set(connection, cursor)
            
            # LC display
            lcd = com_ssd1306.SSD1306()
            lcd.text(1, 5, 'Temp: ' + str(instance.temperature()) + '°C', 2)
            lcd.text(1, 20, 'Hum: ' + str(instance.humidity()) + '%', 2)
            
            self.lock.release()

            time.sleep(delay)
