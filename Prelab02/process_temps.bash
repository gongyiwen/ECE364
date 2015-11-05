#! /bin/bash
$Author: ee364e03 $
#$Date: 2015-09-05 16:34:37 -0400 (Sat, 05 Sep 2015) $
#$Revision: 81403 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab02/process_temps.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

if (( $# != 1 ))
then
echo "Usage: process_temps.bash <input file>"
exit 1
fi

if [[ ! -r $1 ]]
then
echo "Error : $1 is not a readable file"
exit 2
fi

header=$(head -n1 $1)
names=($header)
number=${#names[*]}
((num=number-1))
ct=0
average=0

while read -a line
do
  ((ct=ct+1))
  if (( ct > 1 ))
  then
    sum=0

    for ((I=1; I <= $num; I++))
    do
      ((sum=sum+${line[$I]}))
    done

    ((average=sum/num))
    echo "Average temperature for time ${line[0]} was $average C."
   fi
  
done < $1

exit 0

