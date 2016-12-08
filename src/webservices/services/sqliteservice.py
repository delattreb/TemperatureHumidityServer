"""
com_sqlite v1.0.3
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import sqlite3

from ladon.compat import PORTABLE_STRING
from ladon.ladonizer import ladonize

from dal import dal_dht22
from lib import com_config, com_logger


class SQLiteService(object):
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        self.connection = sqlite3.Connection(self.config['SQLITE']['database'])
        self.logger = com_logger.Logger('SQLite')
        
        self.cursor = self.connection.cursor()
        self.database = self.config['SQLITE']['database']
    
    def __del__(self):
        pass
        # self.connection.close()
        # self.cursor.close()
    
    @ladonize(PORTABLE_STRING, PORTABLE_STRING, rtype = int)
    def inserttemphum(self, temp, hum):
        try:
            connection = sqlite3.Connection(self.database)
            cursor = connection.cursor()
            
            dal = dal_dht22.DAL_DHT22(connection, cursor)
            dal.set_dht22(self.config['GPIO']['DHT22_INTERIOR_NAME'], temp, hum)
            
            self.logger.debug('Database: ' + temp + ' ' + hum)
            return 0
        except Exception as exp:
            self.logger.error(repr(exp))
            return -1
