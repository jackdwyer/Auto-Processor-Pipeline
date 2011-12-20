"""Jack Dwyer
19/12/2011
Base process class, all functions for the framework will be derived from
"""

class Proc():
    def process(self, file, data):
        raise Exception("You must overide this method!")
    
    def run(self, file, data, **args):
        data = self.process(file, data, **args) 
        return data