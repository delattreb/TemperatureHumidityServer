"""
thread_acquisition_dht11.py v1.0.0
Auteur: Bruno DELATTRE
Date : 17/09/2016
"""

import sqlite3
import threading
import time

from lib import com_config, com_lcd, com_logger
from lib.driver import com_dht22


class ThreadAcquisitionDHT22(threading.Thread):
    def __init__(self, name, lock, port, delay, delayread, delayws, counter, ledport, infiny = False):
        super().__init__()
        conf = com_config.Config()
        config = conf.getconfig()
        self.name = name
        self.port = port
        self.ledport = ledport
        self.counter = counter
        self.delay = delay
        self.delayread = delayread
        self.delayws = delayws
        self.lock = lock
        self.infiny = infiny
        self.database = config['SQLITE']['database']
    
    def run(self):
        logger = com_logger.Logger('DHT22:' + self.name)
        logger.info('Start')
        self.gettemphum()
        logger.info('Stop')
    
    def gettemphum(self):
        instance = com_dht22.DHT22(self.port, self.ledport)
        lcd = com_lcd.LCD()
        cpt = 0
        cptws = 0
        temp = 0
        hum = 0
        nextacq = time.time()
        while self.counter or self.infiny:
            if time.time() >= nextacq:
                nextacq += self.delay
                self.lock.acquire()
        
                # Database connection
                connection = sqlite3.Connection(self.database)
                cursor = connection.cursor()
        
                if cptws > self.delayws:
                    instance.recorddata(self.name, connection, cursor)
                    cptws = 0
        
                if cpt > self.delayread:
                    temp, hum = instance.read()
                    cpt = 0
        
                lcd.displaysensor(temp, hum, cpt, self.delayread, cptws, self.delayws)
                cpt += 1
                cptws += 1
        
                self.lock.release()
        
                if not self.infiny:
                    self.counter -= 1
            time.sleep(0.1)
