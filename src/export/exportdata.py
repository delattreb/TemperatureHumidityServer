"""
exportdata.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 09/12/2016
"""

from dal import dal_dht22
from lib import com_config, com_logger, com_sqlite


class ExportData:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        
        self.logger = com_logger.Logger('Export Data')
        
        sqlite = com_sqlite.SQLite(True)
        self.connexion = sqlite.connection
        self.cursor = sqlite.cursor
    
    def export(self):
        self.logger.info('Get data from database')
        dal = dal_dht22.DAL_DHT22(self.connexion, self.cursor)
        rows = dal.get_dht22()
        
        self.logger.info('Write file')
        # TODO read last line and send date to req
        file = open(self.config['EXPORT']['file'], 'a+')
        for row in rows:
            file.write(row[0] + ',' + row[1] + ',' + str(row[2]) + ',' + str(row[3]) + '\n')
        file.close()
        self.logger.info('Export done: ' + self.config['EXPORT']['file'])
