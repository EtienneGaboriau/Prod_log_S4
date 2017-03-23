#!/usr/bin/env python
#classe Installation

class Installation:

    def __init__(self, num, name, code, ville, lati, longi):
        self.num = num
        self.nom = name
        self.code_postal = code
        self.ville = ville
        self.latitude = lati
        self.longitude = longi

    def __repr__(self):
        return "({0} - {1})".format(self.nom, self.num)
