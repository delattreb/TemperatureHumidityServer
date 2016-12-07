"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 7/12/2016
"""

from webservices import serverwebservices
from lib import com_config

conf = com_config.Config()
conf.setconfig()

server = serverwebservices.ServerWebServices()
server.run()
