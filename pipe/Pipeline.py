class Pipeline():
        
    def __init__(self, *modules):   
        self.instanceDict = {}
        self.data = {}
        self.sequenceList = []
        self.total = 0
        
        #NEED TO PASS PARMS from the engine
        self.file = ""
        
        
        
        for mod in modules:
            self.sequenceList.append(mod)
        #print "** PASSED MODS **"
        #print self.sequenceList
    
    def create(self):       
        self.instanceModules()

    def instanceModules(self):
        for class_ in self.sequenceList:
            module = __import__(class_)
            mod = getattr(module, class_)
            x = mod()
            self.instanceDict[class_] = x
    
    def run(self, file):
        self.total += 1
        self.file = file
        for clazz in self.sequenceList:
            self.data = self.instanceDict[clazz].run(self.file, self.data)
            
    def getMods(self):
        return self.sequenceList

    def getData(self):
        return self.data
    
    def finalise(self):
        print self.total
        print self.data