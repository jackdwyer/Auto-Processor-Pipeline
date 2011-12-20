"""
Jack Dwyer
20/12/2011

SAX Auto Processor Engine
Grabs images and passes them to correct pipeline
"""

import yaml
import os, sys
from Pipeline import Pipeline

#for simple sim
import threading
from generateImages import generateImages

class simThread(threading.Thread):
    def run(self, numberOfImages):
        try:
            generateImages(numberOfImages)
        except KeyboardInterrupt:
            raise


#Get all Experiment Parameters, and configs
def start(yamlConfig):
    stream = file(yamlConfig, 'r')
    config = yaml.load(stream)
    pipes = config.get('imageTypes')
    pipeConfig = config.get('pipeConfig')
    #Generate the specified pipelines
    pipelines = buildPipelines(pipes, pipeConfig)

    #Will use this to know when experiment has finished
    numberOfImages = 100

    """START A SIMULATION """
    t = simThread()
    t.run(numberOfImages)
    
    
    
    print "********* pipes build - NOW RUNNING ************"
    for pipe in pipes:
        print pipe
        pipe.run()
        print pipe.getMods()
    



def buildPipelines(pipes, config):
    """
    Generate pipelines
    """
    pipesDict = {}
    for pipe in pipes:
        print pipe
        try :
            parms = pipeConfig[pipe]
        except :
            parms = {}  
        x = Pipeline(*parms)      
        x.create()
        pipesDict[pipe] = x
    return pipesDict


if __name__ == "__main__":   
    if 'build' in sys.argv: 
        start(sys.argv[2])






