#!/bin/bash

export PATH=/usr/sbin:/sbin:/usr/bin:/bin

if [ "$#" != "1" ]; then
    echo "Usage: $0 <Method of Delete>"
    exit 1
fi
echo $1
if [ "$1" = "[Cc][Ss][Vv]" ]; then 
    echo cats
    read file     
    exit 0
fi

#if [ "$1" = "" ] 
    
#fi


    read file     



##################CVS####################3

#
# The students' real names -- NO COMMAS
#
realNames=(`cut -d, -f1,2 $file`)
echo -e REALNAMES: #${realNames[@]}
printf -- '%s\n' "${realNames[@]}"
echo ${#realNames[@]}
#
# The students' usernames
#
usernames=(`cut -d, -f3 $file`)
#echo ${usernames[@]}
echo -e USERNAMES:
printf -- '%s\n' "${usernames[@]}"
echo ${#usernames[@]}
echo ""
#
# The students' classification i.e. CS, minor, Math340 
#
types=(`cut -d, -f4 $file`)
echo -e TYPES:
#printf -- '%s\n' "${types[@]}"
echo ${types[@]}

year=$1
echo
echo year: $year
echo

















































#
# The students' real names
#
#realNames=(
#"John Asawacharoenkun"
#)


#
# The students' usernames
#
#usernames=(
#"jasawacharoenkun1"
#)

#types=(
#"CS"
#)

#year=2014

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
confirm="N"
sudo cat /dev/null
if [[ $? == 0 ]]; then
    echo "confrim deletion [y|n]"
    read confirm
    for ((i = 0; i < ${#realNames[*]}; ++i)); do
        name="${realNames[$i]}"
        user="${usernames[$i]}"
	    other="${types[$i]},${year}"
        if [[ $confirm = "y" ]]; then 
            #sudo deluser ${user};
    	    echo deleting ${user}
            #sudo rm -rf /home/${user};
        fi
    done
else
    echo "ERROR: Root access is required"
    exit 2
fi

#
# All done!
#
exit 0
