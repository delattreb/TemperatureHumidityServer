"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 7/12/2016
"""



from lib import com_config
from webservices import clientwebservices

conf = com_config.Config()
conf.setconfig()


client = clientwebservices.ClientWebServices()
client.getlistAlbums()


