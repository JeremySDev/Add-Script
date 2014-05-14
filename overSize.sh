#!/bin/bash

export PATH=/usr/sbin:/sbin:/usr/bin:/bin
#KB
warningSize=50000

#find '/home' -size +$warningSize  | cut -d"/" -f3 | sort -u
#files=(`find '/home' -size +$warningSize  | sort -u`)
#find '/home' -size +$warningSize  | sort -u 

fileOwner=(`find '/home' -size +$warningSize  | cut -d"/" -f3`)
fileName=(`find '/home' -size +$warningSize  | cut -d"/" -f3`)
echo -e fileOwner: ${fileOwner[@]} fileName: ${fileName[@]} 
