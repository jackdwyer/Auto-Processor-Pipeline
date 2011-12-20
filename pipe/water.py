"""Jack Dwyer
20/12/2011
"""

from Proc import Proc

class water(Proc):
    def process(self, file, data):
        print "MODULE - WATER"
        return data