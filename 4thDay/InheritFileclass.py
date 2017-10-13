import fileinfo
import os

class NewFileinfo(fileinfo.Fileinfo):
    def getextension(self):
        return os.path.splitext(self.nameoffile) [-1]
