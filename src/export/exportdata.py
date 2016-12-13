"""
exportdata.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 09/12/2016
"""

import os

from dal import dal_dht22
from lib import com_config, com_email, com_logger, com_sqlite


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
        lastdatarows = dal.get_lastdata()
        self.logger.info('Write file')
        
        # Read last line and send date to req
        if os.path.isfile(self.config['EXPORT']['lastexport']):
            file = open(self.config['EXPORT']['lastexport'], 'r')
            lastdate = file.read()
            file.close()
            rows = dal.get_dht22(str(lastdate))
        else:
            lastdate = '2000-01-01 00:00:00'
            rows = dal.get_dht22(lastdate)
        
        if not os.path.isfile(self.config['EXPORT']['file']):
            # Creaate Data file
            file = open(self.config['EXPORT']['file'], 'w')
            file.write('Date,Capteur,Temperature,Humidite\n')
            file.close()
        
        if rows:
            file = open(self.config['EXPORT']['file'], 'a+')
            for row in rows:
                file.write(row[0] + ',' + row[1] + ',' + str(row[2]) + ',' + str(row[3]) + '\n')
            file.close()
            self.logger.info('Export done: ' + self.config['EXPORT']['file'])
        
        # Create ast entry
        if lastdatarows[0][0]:
            file = open(self.config['EXPORT']['lastexport'], 'w')
            file.write(lastdatarows[0][0])
            file.close()
        
        # Send mail if no new record
        if not rows:
            mail = com_email.Mail()
            table = ['Since:' + lastdate]
            mail.send_mail_gmail('Temp Hum: No DATA', table)
