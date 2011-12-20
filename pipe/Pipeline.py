class Pipeline():
    
    data = {}
    instanceDict = {}
    sequenceList = []
    
    def create(self, *modules):
        print "******* mods passed ***********"
        for x in modules:
            print x
        
        self.instanceModules(modules)


    def instanceModules(self, modules):
        for class_ in modules:
            module = __import__(class_)
            mod = getattr(module, class_)
            x = mod()
            self.instanceDict[class_] = x
            self.sequenceList.append(class_)
    
    def run(self):
        for clazz in self.sequenceList:
            self.data = self.instanceDict[clazz].run()

    
    def getData(self):
        return self.data