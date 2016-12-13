"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : //2017
"""

from webservices import clientwebservices
# Call WebServices
client = clientwebservices.ClientWebServices()
ret = client.inserttemphum('test', '10.1', '50.1')

print(0)
