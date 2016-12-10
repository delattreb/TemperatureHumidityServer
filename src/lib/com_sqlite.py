"""
com_sqlite v1.0.3
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import sqlite3

from lib import com_config


class SQLite:
    def __init__(self, copy = False):
        conf = com_config.Config()
        self.config = conf.getconfig()
        
        if copy:
            self.connection = sqlite3.Connection(self.config['SQLITE']['databasecopy'])
        else:
            self.connection = sqlite3.Connection(self.config['SQLITE']['database'])

        self.cursor = self.connection.cursor()
    
    def __delete__(self, instance):
        self.connection.close()
        self.cursor.close()
