class Pipeline():
        
    def __init__(self, *modules):   
        self.instanceDict = {}
        self.data = {}
        self.sequenceList = []
        self.total = 0
        
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
    
    def run(self):
        self.total += 1
        for clazz in self.sequenceList:
            self.data = self.instanceDict[clazz].run()
            
    def getMods(self):
        return self.sequenceList

    def getData(self):
        return self.data
    
    def finalise(self):
        print self.total