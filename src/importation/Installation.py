#!/usr/bin/env python
#classe Installation

class Installation:

    def __init__(self, num, name, addr, code, lati, longi):
        self.num = num
        self.nom = name
        self.addresse = addr
        self.code_postal = code
        self.latitude = lati
        self.longitude = longi

    def __repr__(self):
        return "({0} - {1})".format(self.nom, self.num)
