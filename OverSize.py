__author__ = 'Jeremy Stilwell'
import os
import subprocess

warningSize = 50000

os.system("find '/home' -size +$warningSize  | cut -d"/" -f3")
#p = subprocess.call("find", "/home", "-size", +warningSize,  | cut -d"/" -f3")