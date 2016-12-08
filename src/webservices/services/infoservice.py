"""
infoservice.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 8/12/2016
"""

from ladon.compat import PORTABLE_STRING
from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType

from lib import com_config


# @ladonize(PORTABLE_STRING, rtype = [Album])
# def listAlbums(self, search_frase = PORTABLE_STRING('')):


class Version(LadonType):
    version = PORTABLE_STRING


class InfoService(object):
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
    
    @ladonize(rtype = [Version])
    def getversion(self):
        v = Version()
        v.version = self.config['WEBSERVICES']['name']
        return v
