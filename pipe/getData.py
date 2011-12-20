"""Jack Dwyer
20/12/2011
test read data from file
"""

from Proc import Proc

class getData(Proc):
    """does a quit and dirty job of reading the headers, and returns a dictionary"""
    def process(self, file, data):
        f = open(file, 'r')
        num = f.read()
        f.close
        d = data
        d[file] = num
        return data