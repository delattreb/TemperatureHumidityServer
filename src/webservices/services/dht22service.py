"""
dht22.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 8/12/2016
"""

from ladon.ladonizer import ladonize

from lib import com_config, com_dht22


class DHT22Service(object):
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
    
    @ladonize(rtype = float)
    def read(self):
        dht22 = com_dht22.DHT22(self.config['GPIO']['DHT22_INTERIOR_PORT'], 'DHT22')
        temp, hum = dht22.read()
        return temp, hum
