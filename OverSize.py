__author__ = 'Jeremy Stilwell'
import commands
import re
from sys import stdin

warningSize = "50000c"
deleteSize = "100000c"

#the name of the directory to run the script on
directory = "''"


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
    num = 6
    for i in files:
        #get length of string
        len1 = i.__len__()
        #gets rid of the characters preceding the username
        #TODO find length of chars preceding username
        temp1 = i[num:len1]
        #turns temp1 in to an array of strings based on a separator /
        temp2 = (temp1.partition('/'))
        #gets the user name out of the array.
        userArray.append(temp2[0])

"""
method called when user array and file array are not hte same size
"""


def size_error():
    print "Size of file list and user list are not the same "
    exit()

#this part of the code deletes files if the user tells it to otherwise it will just warn
#it doesn't actual delete files but moves them to a file in the directory of the script
########################################################################################################################
delete = commands.getoutput("find " + directory + " -size +" + deleteSize)
########################################################################################################################
print "files 100000 and above"
turn_array(delete)
find_users(fileArray)
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

#this part of the code gives users a warning
########################################################################################################################
warn = commands.getoutput("find " + directory + " -size +" + warningSize)
########################################################################################################################
turn_array(warn)
find_users(fileArray)
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
