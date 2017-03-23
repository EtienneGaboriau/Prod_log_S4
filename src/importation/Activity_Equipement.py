#!/usr/bin/env python
#classe Activity

class Activity_Equipement:

    def __init__(self, numAct, numEqu):
        self.numAct = numAct
        self.numEqu = numEqu

    def __repr__(self):
        return "({0} - {1})".format(self.numAct, self.numEqu)
