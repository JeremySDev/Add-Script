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


def turn_array(com):
    #iterator
    j = 0

    global varfilename

    for i in com:
        varfilename += i
        if i == '\n' or j == (f.__len__() - 1):
            varfilename = varfilename.rstrip('\n')
            fileArray.append(varfilename)
            varfilename = ""
        #print "vfn: ", varfilename
        j += 1
        #print "j: ", j

#print "f: ", f
print "array: ", fileArray

print
print "files 100000 and above"
os.system("find '/home/jstilwell/test' -size +" + deleteSize)
#returns exit status
#print p