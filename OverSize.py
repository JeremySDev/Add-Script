__author__ = 'Jeremy Stilwell'
import os

warningSize = "75000c"
deleteSize = "100000c"

print "files 50000 and above"
os.system("find '/home/jstilwell/test' -size +" + warningSize)
os.popen("find '/home/jstilwell/test' -size +" + warningSize)



print "files 100000 and above"
os.system("find '/home/jstilwell/test' -size +" + deleteSize)
#returns exit status
#print p