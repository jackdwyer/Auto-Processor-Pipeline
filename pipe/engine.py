"""
Jack Dwyer
20/12/2011

SAX Auto Processor Engine
Grabs images and passes them to correct pipeline
"""

import yaml
import os, sys
from Pipeline import Pipeline

#Get all Experiment Parameters, and configs
def start(yamlConfig):
    stream = file(yamlConfig, 'r')
    config = yaml.load(stream)
    pipes = config.get('imageTypes')
    pipeConfig = config.get('pipeConfig')
    #Generate the specified pipelines
    pipelines = buildPipelines(pipes, pipeConfig)

    """START A SIMULATION """
    



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






