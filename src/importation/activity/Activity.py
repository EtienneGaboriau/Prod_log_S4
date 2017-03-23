#!/usr/bin/env python
#classe Activity

class Activity:

    def __init__(self, nameAct, numAct):
        self.name = nameAct
        self.num = numAct

    def __repr__(self):
        return "({0} - {1})".format(self.name, self.num)
