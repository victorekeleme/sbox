import random
import os
import socket

def ranPath():
    codeGen ='122'+ str(random.randint(1000,10000))
    currentPath = os.path.dirname(os.path.abspath(__file__))
    #hostname=socket.gethostname()
    #IPAddr=socket.gethostbyname(hostname)
    
    downloadPath = currentPath+'/'+codeGen
    return downloadPath

