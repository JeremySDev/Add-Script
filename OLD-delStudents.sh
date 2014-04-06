#!/bin/bash

export PATH=/usr/sbin:/sbin:/usr/bin:/bin

#
# The students' real names
#
realNames=(
"Test Student"
)


#
# The students' usernames
#
usernames=(
"testytest"
)

types=(
"Semester"
)

year=2013

#
# Make sure that both the 'realNames' and 'usernames' arrays are the same size.
# They should be because usernames[i] is the user name for the person with
# name[i].
#
if [[ ${#realNames[*]} != ${#usernames[*]} ]]; then
    echo "Number of users does not match number of usernames"
    exit 1
fi

#
# Now we know the the length of the realNames and usernames arrays are the same.
# We need a third array of passwords that is the same size.  This array will
# correspond the passwords for each user (i.e., the password for realNames[i]
# will be passwords[i].
#

#
# Make sure that we can sudo successfully
#
sudo cat /dev/null
if [[ $? == 0 ]]; then
    for ((i = 0; i < ${#realNames[*]}; ++i)); do
        name="${realNames[$i]}"
        user="${usernames[$i]}"
	other="${types[$i]},${year}"

	sudo deluser ${user};
	sudo rm -rf /home/${user};
    done
else
    echo "ERROR: Root access is required"
    exit 2
fi

#
# All done!
#
exit 0
