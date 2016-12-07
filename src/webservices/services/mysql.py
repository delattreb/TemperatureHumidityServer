"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 7/12/2016
"""
"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 7/12/2016
"""

from ladon.ladonizer import ladonize


class MySQL(object):
    @ladonize(int, int, rtype = int)
    def add(self, a, b):
        return a + b
