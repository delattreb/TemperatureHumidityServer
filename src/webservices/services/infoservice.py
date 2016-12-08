"""
infoservice.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 8/12/2016
"""

from ladon.ladonizer import ladonize

from lib import com_config


class InfoService(object):
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        
    @ladonize(type = str)
    def getversion(self):
        return self.config['WEBSERVICES']['version']
