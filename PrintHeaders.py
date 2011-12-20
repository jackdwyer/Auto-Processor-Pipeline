"""Jack Dwyer
19/12/2011
Prints the data dictionary 
"""

from Proc import Proc

class PrintHeaders(Proc):
    def process(self, file, data):
        print "******************************* Printing Headers *******************************"
        for x in data:
            print x + ":" + data[x]