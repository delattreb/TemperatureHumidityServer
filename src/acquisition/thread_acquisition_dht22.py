"""
thread_acquisition_dht11.py v1.0.0
Auteur: Bruno DELATTRE
Date : 17/09/2016
"""

import sqlite3
import threading
import time

import lcd
from lib import com_config, com_dht22, com_logger


class ThreadAcquisitionDHT22(threading.Thread):
    def __init__(self, name, lock, port, delay, delayread, counter, ledport, infiny=False):
        super().__init__()
        conf=com_config.Config()
        config=conf.getconfig()
        self.name=name
        self.port=port
        self.ledport=ledport
        self.counter=counter
        self.delay=delay
        self.delayread=delayread
        self.lock=lock
        self.infiny=infiny
        self.database=config['SQLITE']['database']
    
    def run(self):
        logger=com_logger.Logger('DHT22:'+self.name)
        logger.info('Start')
        self.gettemphum()
        logger.info('Stop')
    
    def gettemphum(self):
        instance=com_dht22.DHT22(self.port, self.ledport)
        l=lcd.LCD()
        cpt=0
        while self.counter or self.infiny:
            self.lock.acquire()
            
            connection=sqlite3.Connection(self.database)
            cursor=connection.cursor()
            if cpt>self.delayread:
                instance.set(self.name, connection, cursor)
                instance.progressbaroff(l)
                cpt=0
            instance.refreshlcd(l, cpt, self.delayread)
            cpt+=1
            self.lock.release()
            
            self.counter-=1
            time.sleep(self.delay)
