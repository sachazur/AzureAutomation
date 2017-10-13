import fileinfo
import os

class Fileinfo:
    def __init__(self,nameoffile):
        self.nameoffile=nameoffile
        self.fileactualinfo = open(self.nameoffile)
    def getsize(self):
        return os.path.getsize(self.nameoffile)
    def getlinecount(self):
        return len(self.fileactualinfo.readlines())
    def getage(self):
        pass
    def getfirstline(self):
        return self.fileactualinfo.readlines(1)
    def getlastline(self):
        pass
    def getnthline(linenumber):
        pass
    def close(self):
        self.fileactualinfo.close()


    
