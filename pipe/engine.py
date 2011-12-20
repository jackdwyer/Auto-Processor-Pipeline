"""
Jack Dwyer
20/12/2011

SAX Auto Processor Engine
Grabs images and passes them to correct pipeline
"""

import yaml
import os, sys
import glob
from Pipeline import Pipeline


#Get all Experiment Parameters, and configs
def start(yamlConfig):
    stream = file(yamlConfig, 'r')
    config = yaml.load(stream)
    pipes = config.get('imageTypes')
    pipeConfig = config.get('pipeConfig')
    print pipeConfig
    #Generate the specified pipelines
    pipelines = buildPipelines(pipes, pipeConfig)
    print "********** pipe lines created ***********"
    print "START SIMULATION WITH > python generateImages.py gen"
    
    #Will use this to know when experiment has finished
    numberOfImages = 100
    
    completedImages = []
    while (len(completedImages) < numberOfImages):        
        #need to check images in location
        images = glob.glob('*.img')
        for image in images:
            if image not in completedImages:
                type = getType(image)
                print type
                print "************************"
                print pipelines[type].getMods()
                print "************************"
                
                pipelines[type].getMods()
                pipelines[type].run()                
                completedImages.append(image)
                print "IMAGE COMPETED: " + image
            else:
                """do nothing """
                
                
                
                
                
                
def getType(fileName):
    #only a quick method to get image type
    values = fileName.split(".")
    values = values[0].split("_")
    return values[2]


def buildPipelines(pipes, config):
    """
    Generate pipelines
    """
    pipesDict = {}
    for pipe in pipes:
        print config
        try :
            parms = config[pipe]
        except :
            parms = {}  
        
        print parms
        x = Pipeline(*parms)      
        x.create()
        pipesDict[pipe] = x
    return pipesDict


if __name__ == "__main__":   
    if 'start' in sys.argv: 
        start(sys.argv[2])






