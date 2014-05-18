__author__ = 'Jeremy Stilwell'
import commands, re
from sys import stdin

warningSize = "50000c"
deleteSize = "100000c"




#holds all filenames
fileArray = []
userArray = []
#turns the output of find into an array
"""
turns the data from a find command in to an array
"""


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


"""
finds the users from an array of files passed in
"""


def find_users(files):
    for i in files:
        len1 = i.__len__()
        temp1 = i[6:len1]
        temp2 = (temp1.partition('/'))
        userArray.append(temp2[0])


def size_error():
    print "Size of file list and user list are not the same "
    exit()

#echo cat | mutt -s "this is a test" jstilwell@agora.cs.wcu.edu
########################################################################################################################
delete = commands.getoutput("find '/home/jstilwell/test' -size +" + deleteSize)
########################################################################################################################
print "files 100000 and above"
turn_array(delete)
find_users(fileArray)
print fileArray
print userArray
########################################################################################################################
if len(fileArray) == len(userArray):
    print
    ####################################################################################################################
    # iterates over the array of files and users so that the user can see if the files should be deleted
    for j in range(0, len(fileArray)):
        print "User: ", userArray[j], " File: ", fileArray[j], "will be deleted."
    # ask if these are these files should be delete
    print "Delete Files [y/N]: "
    userinput = stdin.read(1)
    if re.match("y|Y", userinput):
    ####################################################################################################################
        for j in range(0, len(fileArray)):
            #f = commands.getstatusoutput("mv " + fileArray[j] + " ./trash")
            #message for the user
            msg = "Your file " + fileArray[j] + " has been removed because it was larger than the allowed size.\n " \
                                                "Please contact your system administrator if you have questions. " \
                                                "This is an automated message."
            commands.getstatusoutput("echo -e " + msg + " | mutt -s 'Your File was Removed' " + userArray[j] +
                                     "@agora.cs.wcu.edu")
            f = "mv " + fileArray[j] + " ./trash"
            print f
    print
    fileArray = []
    userArray = []
else:
    size_error()
########################################################################################################################
warn = commands.getoutput("find '/home/jstilwell/test' -size +" + warningSize)
########################################################################################################################
print "files 50000 and above"
turn_array(warn)
find_users(fileArray)
print fileArray
print userArray
########################################################################################################################
if len(fileArray) == len(userArray):
    print
    # iterates over the array of files and users so that they can be informed of their heinous crime
    for j in range(0, len(fileArray)):
        msg = "Your file " + fileArray[j] + "is larger than the recommended size.\n " \
                                            "Please contact your system administrator if you have questions. " \
                                            "This is an automated message."
        commands.getstatusoutput("echo -e " + msg + " | mutt -s 'Your File is Oversize' " + userArray[j] +
                                 "@agora.cs.wcu.edu")
else:
    size_error()
########################################################################################################################
print