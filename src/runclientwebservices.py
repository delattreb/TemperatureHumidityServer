"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 7/12/2016
"""

from webservices import clientwebservices
from lib import com_config

conf = com_config.Config()
conf.setconfig()

client = clientwebservices.ClientWebServices()
client.getcalculator()
client.getmysql()
