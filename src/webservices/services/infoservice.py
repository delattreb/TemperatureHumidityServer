"""
infoservice.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 8/12/2016
"""

from ladon.compat import PORTABLE_STRING
from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType

from lib import com_config


class Version(LadonType):
    name = PORTABLE_STRING
    description = PORTABLE_STRING
    version = PORTABLE_STRING


class InfoService(object):
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
    
    @ladonize(rtype = [Version])
    def getversion(self):
        version = []
        v = Version()
        v.name = self.config['WEBSERVICES']['name']
        v.description = self.config['WEBSERVICES']['description']
        v.version = self.config['WEBSERVICES']['version']
        version += [v]
        return version

"""
    @ladonize(PORTABLE_STRING, rtype = [Version])
    def getversion(self, search_frase = PORTABLE_STRING('')):
        version = []
        v = Version()
        v.name = self.config['WEBSERVICES']['name']
        v.description = self.config['WEBSERVICES']['description']
        v.version = self.config['WEBSERVICES']['version']
        version += [v]
        return version

"""
