#!/bin/bash

export PATH=/usr/sbin:/sbin:/usr/bin:/bin

#
# The students' real names -- NO COMMAS
#
realNames=(
"John Asawacharoenkun"
"Amber Briggs"
"Tyler Elliot"
"Abigail Emrey"
"Dylan Foster"
"Meghan Galvin"
"Tommy Ho"
"Charles Hreha"
"Ian Johnson",
"Jordan Joseph"
"Kerrie Kaiser"
"Clinton Langston"
"Brandon Piasecki"
"Devin Ricker"
"David Schumerth"
"Sarah Simpson"
"Avery Sluder"
"Clifton West"
"Christopher Wolf"
"Terry Mitchell"
"Jon Johnson"
)


#
# The students' usernames
#
usernames=(
"jasawacharoenkun1"
"anbriggs1"
"trelliot1"
"aekmrey1"
"dwfoster1"
"mbgalvin"
"tho2"
"cahreha1"
"injohnson2",
"jcjoseph2"
"kakaiser1"
"cmlangston"
"bjpiasecki"
"dsricker"
"daschumerth1"
"sesimpson1"
"adsluder1"
"cwest2"
"crwolf1"
"tjmitchell1"
"jwjohnson7"
)

types=(
"CS"
"CS"
"CS"
"PreCS"
"PreCS"
"CS"
"CS"
"CS"
"CS"
"Minor"
"Minor"
"PreCS"
"PreCS"
"CS"
"EE"
"Minor"
"CS"
"CS"
"Music"
"CS"
"CS"
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

        #
        # Test to see if this users exists already.  'id' will exit with 0 if a
        # user with the specified username exists, non-zero otherwise.  We want
        # the non-zero case.
        #
        id ${user} &> /dev/null
        if [[ $? != 0 ]]; then
     	    # Generate a random passwd and check validity using cracklib-check
	    okay="NotOK"
            until [[ "$okay" == "OK" ]]; do
		pass=$(makepasswd --chars 8)
		result="$(cracklib-check <<<"$pass")"
		okay="$(awk -F': ' '{ print $2}' <<<"$result")"
	    done

            # Create the user
            sudo adduser --disabled-password --gecos "${name},${other}" "${user}"

	    # Add user to student group
	    sudo adduser "${user}" student

            # Set the new user's password
            echo "${user}":"${pass}" | sudo chpasswd
	    
            # Expire the new user's password -- make them change it the first
            # time they log in.
            #
            sudo chage -d0 "${user}"

            # Remove read permissions from their home directory.
            sudo chmod 701 /home/${user}

	    # Set user disk quota
	    sudo setquota -u "${user}" 10485760 11010048 50000 55000 /home

            # Print the information for the user.
            echo   ""
            echo   "------------------------------------------------------------"
            printf "%-30s %-20s %-8s\n"  "${name}"  "${user}"  "${pass}"
            echo   "------------------------------------------------------------"
            echo   ""
        else
            echo "WARN: User ${user} already exists."
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
