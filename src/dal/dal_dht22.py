"""
dal_dht11 v1.0.0
Auteur: Bruno DELATTRE
Date : 19/09/2016
"""

from lib import com_logger


class DAL_DHT22:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
        self.logger = com_logger.Logger('DHT22 DAL')
    
    """ Select"""
    
    def get_dht22(self):
        try:
            self.cursor.execute('SELECT date, name, temperature, humidity FROM DHT22')
            rows = self.cursor.fetchall()
            return rows
        except Exception as exp:
            self.logger.error(repr(exp))
            self.connection.rollback()
    
    """ Insert """
    
    def set_dht22(self, name, temperature, humidity):
        try:
            self.cursor.execute(
                'INSERT INTO  DHT22 (date, name, temperature, humidity) VALUES (datetime("now","localtime"),"' + str(name) + '","' + str(temperature) + '","' + str(
                    humidity) + '")')
            self.connection.commit()
        except Exception as exp:
            self.logger.error(repr(exp))
            self.connection.rollback()
