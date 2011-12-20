"""
Jack Dwyer 20/12/2011
Uses:
http://pyyaml.org/wiki/PyYAMLDocumentation
easy_install pyYaml

"""
import yaml
import os, sys

from Pipeline import Pipeline

def build(config):
    stream = file(config, 'r')
    config = yaml.load(stream)
    pipes = config.get('pipes')
    pipeConfig = config.get('pipeConfig')
    pipesList = []
    
    for pipe in pipes:
    
        try :
            parms = pipeConfig[pipe]
        except :
            parms = {}  
        x = Pipeline(*parms)      
        x.create()
        pipesList.append(x)
    
    print pipesList
    return pipesList

def create(config):
    pipes = build(config)
    print pipes
    print "********* pipes build - NOW RUNNING ************"
    for pipe in pipes:
        print pipe
        pipe.run()
        print pipe.getMods()

if __name__ == "__main__":    
    if 'build' in sys.argv:
            create(sys.argv[2])
