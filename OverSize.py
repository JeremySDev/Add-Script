__author__ = 'Jeremy Stilwell'
import commands
import os

warningSize = "75000c"
deleteSize = "100000c"

#os.system("find '/home/jstilwell/test' -size +" + warningSize)
print "files 50000 and above"
warn = commands.getoutput("find '/home/jstilwell/test' -size +" + warningSize)
delete = commands.getoutput("find '/home/jstilwell/test' -size +" + deleteSize)

#holds all filenames
fileArray = []

#turn the output of find into an array


def turn_array(com):
    #iterator
    j = 0

    #stores the name of file being built
    global varfilename
    varfilename = ""

    for i in com:
        varfilename += i
        if i == '\n' or j == (com.__len__() - 1):
            varfilename = varfilename.rstrip('\n')
            fileArray.append(varfilename)
            varfilename = ""
        j += 1
turn_array(warn)
print "array: ", fileArray

print
print "files 100000 and above"
os.system("find '/home/jstilwell/test' -size +" + deleteSize)
#returns exit status
#print p