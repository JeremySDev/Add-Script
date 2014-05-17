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
user_array = []
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


def find_users(files):
    for i in files:
        len1 = i.__len__()
        temp1 = i[6:len1]
        temp2 = (temp1.partition('/'))
        user_array.append(temp2[0])

print "files 50000 and above"
turn_array(warn)
find_users(fileArray)
print fileArray
print user_array
print
fileArray = []
user_array = []

print "files 100000 and above"
turn_array(delete)
find_users(fileArray)
print fileArray
print user_array