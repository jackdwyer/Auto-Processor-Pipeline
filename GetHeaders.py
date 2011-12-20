"""Jack Dwyer
19/12/2011
Reads the headers from the image files
"""

from Proc import Proc

class GetHeaders(Proc):
    """does a quit and dirty job of reading the headers, and returns a dictionary"""
    def process(self, file, data):
        print "******************************* Reading Headers ************************"
        f = open(file, 'r+')
        header = f.read(512)
        f.close()
        header = header.replace('{','')
        header = header.replace('}','')
        header = header.strip()
        for item in header.split('\n'):
            value1, value2 = item.split("=")
            data[value1] = value2       
        return data