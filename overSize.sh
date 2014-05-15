#!/bin/bash

export PATH=/usr/sbin:/sbin:/usr/bin:/bin
#KB
warningSize=50000

#find '/home' -size +$warningSize  | cut -d"/" -f3 | sort -u
#files=(`find '/home' -size +$warningSize  | sort -u`)
#find '/home' -size +$warningSize  | sort -u 

fileOwner=(`find '/home' -size +$warningSize  | cut -d"/" -f3`)
fileName=(`find '/home' -size +$warningSize`)
#echo -e fileOwner: ${fileOwner[@]} fileName: ${fileName[@]} 

for i in "${fileName[@]}"
do
 #   echo $i
    #printf -- '%s\n' "i"
    printf -- '%s\n' "${fileOwner[@]}"
    #printf -- '%s\n' "${fileName[i]}" 
done
#look in to using these commands but with python for ease of iteration
