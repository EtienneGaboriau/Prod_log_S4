#!/usr/bin/env python
#classe Installation

class Equipement:

    def __init__(self, num, name, num_i):
        self.num = num
        self.nom = name
        self.num_instal = num_i

    def __repr__(self):
        return "({0} - {2})".format(self.nom, self.num, self.num_instal)
