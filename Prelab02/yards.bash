#! /bin/bash
$Author: ee364e03 $
#$Date: 2015-09-05 16:39:23 -0400 (Sat, 05 Sep 2015) $
#$Revision: 81404 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab02/yards.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

if (( $# != 1)) 
then
  echo "Usage: yards.bash <filename>"
elif [[ ! -r $1 ]]
then
  echo "Error: $1 is not readable"
else
highest=0
while read -a line
do
 ((number=${#line[*]}-1))
 name=${line[0]}
 sum=0

 for ((I=1; I <= $number; I++))
 do
 ((sum=sum+${line[$I]}))
 done

 ((average=sum/number))
 X=0
 a=0
 b=0

 for ((I=1; I <= $number; I++))
 do
 ((a=${line[$I]}-average))
 ((b=a**2))
 ((X=X+b))
 done

 ((X=X/number))

   if (( average > highest ))
   then
     highest=$average
   fi
 echo "$name schools averaged $average yards receiving with a variance of $X"
done < $1
echo "The largest average yardage was $highest"
fi
exit 0



