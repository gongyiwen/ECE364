#! /bin/bash
$Author: ee364e03 $
#$Date: 2015-09-08 17:29:44 -0400 (Tue, 08 Sep 2015) $
#$Revision: 81712 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Lab02/printUsageStats.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

if (( $# != 1 ))
then
echo "Usage: ./printUsageStats.bash <filename>"
exit 1
fi

if [[ ! -e $1 ]]
then
echo "Error: $1 does not exist"
exit 2
fi

tmstmp=$(head -c 14 $1 | tail -c 8)
usernumber=$(head -c 37 $1 | tail -c 3)
highCPUp=$(head -n 8 $1 | tail -n 1 | cut -d' ' -f9)
highCPUn=$(head -n 8 $1 | tail -n 1 | cut -d' ' -f2)
first1=$(tail -n +8 $1 | sort -k11 -r -n | head -n 1)
first2=$(tail -n +8 $1 | sort -k11 -r -n | head -n 2| tail -n 1)
first3=$(tail -n +8 $1 | sort -k11 -r -n | head -n 3| tail -n 1 )

echo "Parsing file "$1". Timestamp: $tmstmp"
echo "Your choices are:"
echo "1) Active user IDs"
echo "2) Highest CPU usage"
echo "3) Top 3 longest running processes"
echo "4) All processes by a specific user"
echo "5) Exit"
input=0

while (( $input != 5 ))
do

echo -n "Please enter your choice: "
read input < /dev/tty

if (( $input == 1 ))
  then
  echo "Total number of active user IDs: $usernumber"
fi

if (( $input == 2 ))
  then 
  echo "User $highCPUn is utilizing the highest CPU resources at $highCPUp%"
fi

if (( $input == 3 ))
  then 
  echo $first1
  echo $first2
  echo $first3
fi

if (( $input == 4 ))
  then 
    echo -n "Please enter a valid username: "
    read username < /dev/tty
    echo -n "Please enter a filename to save user's processes: "
    read ofile < /dev/tty
    if grep $username $1 > /dev/null
      then
        grep $username $1 > $ofile
    else
      echo "No Match found"
    fi
fi

if (( $input == 5 ))
then 
  break
fi

done


exit 0

