from ladon.ladonizer import ladonize

"""
.py v 1.0.0
Auteur: Bruno DELATTRE
Date : 7/12/2016
"""


class Calculator(object):
    @ladonize(int, int, rtype = int)
    def add(self, a, b):
        return a + b
