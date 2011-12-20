"""Jack Dwyer
20/12/2011
"""

from Proc import Proc

class dirt(Proc):
    def process(self, file, data):
        print "MODULE - DIRT"
        return data