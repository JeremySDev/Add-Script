__author__ = 'Jeremy Stilwell'
import commands
import os

warningSize = "75000c"
deleteSize = "100000c"

#os.system("find '/home/jstilwell/test' -size +" + warningSize)
print "files 50000 and above"
f = commands.getoutput("find '/home/jstilwell/test' -size +" + warningSize)

#name of file being built
varfilename = ""

#holds all filenames
fileArray = []
for i in f:
    if i == '\n':
        fileArray.append(varfilename)
        varfilename = ""
    else:
        varfilename += i
    print varfilename


print "f: ", f
print "array: ", fileArray


print
print "files 100000 and above"
os.system("find '/home/jstilwell/test' -size +" + deleteSize)
#returns exit status
#print p