from os import walk
import os
import sys

class AntiSpammers:
    def __init__(self):
        pass
    def StartScanning(self):
        f = []
        htmlFiles = []
        for (dirpath, dirnames, filenames) in walk(sys.argv[1]):
            f.extend(filenames)
            for eachFile in f:
                if eachFile.endswith(".htm") or eachFile.endswith(".html"):
                    htmlFiles.append(os.path.join(sys.argv[1],eachFile))
            break
        for eachFile in htmlFiles:
            print eachFile
            f = open(eachFile,"r")
            contents = f.read()
            freshContents = contents
            indexOfScript = contents.find('<SCRIPT Language=VBScript>')
            if indexOfScript != -1:
                freshContents = contents[:indexOfScript]
#            print indexOfScript
            f.close()
            os.remove(eachFile)
            f = open(eachFile,"wb")
            f.write(freshContents)
            f.close()
antiSpammers = AntiSpammers()
antiSpammers.StartScanning()
        
    