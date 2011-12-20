"""Jack Dwyer
19/12/2011
Test for reading additional parameters from the YAML config """


from Proc import Proc

class testAdditionalParms(Proc):
    def process(self, file, data, value1, value2, value3):
        print "******************************* Additional Values_test ****************"
        print str(value1)
        print str(value2)
        print str(value3)
        
        return data