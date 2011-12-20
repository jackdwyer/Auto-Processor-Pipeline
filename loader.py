"""
Jack Dwyer 19/12/2011
Uses:
http://pyyaml.org/wiki/PyYAMLDocumentation
easy_install pyYaml

Some framework/autoloaderme that the big wigs may use at the Monash Sync.
"""
import yaml
import os, sys


def create():
    #possible YAML config creator
    print "create"

def load(config):
    stream = file(config, 'r')
    config = yaml.load(stream)
    #get data file location and classes used
    dataFile = config.get('file')
    modules = config.get('modules')    
    moduleConfig = config.get('moduleConfig')
    instanceDict, sequenceList = initModules(modules)
    data = {}
    run(instanceDict, dataFile, data, moduleConfig, sequenceList);
        
def initModules(modules): 
    instanceDict = {}
    sequenceList = []
    for class_ in modules:
        module = __import__(class_)
        mod = getattr(module, class_)
        x = mod()
        instanceDict[class_] = x
        sequenceList.append(class_)
    return instanceDict, sequenceList

def run(instanceDict, dataFile, data, moduleConfig, sequenceList):
    for class_ in sequenceList:
        try :
            parms = moduleConfig[class_]
        except :
            parms = {}
        data = instanceDict[class_].run(dataFile, data, **parms)

if __name__ == "__main__":    
    if 'create' in sys.argv:
        create()
    if 'load' in sys.argv:
        if (len(sys.argv) <= 2):
            print "Not Enough Arguments: python loader.py load [configFile]"
            sys.exit(1)
            
        if (len(sys.argv) == 3):
            load(sys.argv[2])
            
        if (len(sys.argv) > 3):
            print "Too Many Arguments: python loader.py load [configFile]"
            sys.exit(1)
            

