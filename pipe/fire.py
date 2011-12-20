"""Jack Dwyer
20/12/2011
"""

from Proc import Proc

class fire(Proc):
    def process(self, file, data):
        print "MODULE - FIRE"
        return data