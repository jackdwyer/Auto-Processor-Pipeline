import random
import glob
import sys, os
import time

def generateImages(numberOfImages, imageTypes):
    random.seed()
    types = imageTypes
    
    for i in range(numberOfImages):
        x = random.randint(0, len(types))
        filename = "IMG_"+str(i+1)+"_"+str(types[x-1])+".img"
        print filename
        randValue = random.randint(0, 1000)
        f = open(filename, "w")
        f.write(str(randValue))
        f.close()
        time.sleep(1)
        
        
def deleteIMGS():
    images = glob.glob('*.img')
    for image in images:
        os.remove(image)
    
    
    
    
if __name__ == "__main__":    
    if 'del' in sys.argv:
        deleteIMGS()
    if 'gen' in sys.argv:
        generateImages()