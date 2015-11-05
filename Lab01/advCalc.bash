#! /bin/bash
#$Author: ee364e03 $
#$Date: 2015-09-01 16:46:13 -0400 (Tue, 01 Sep 2015) $
#$Revision: 81253 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Lab01/advCalc.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

if (($# != 1 ))
then
echo "Usage: ./advCalc.bash <filename>"
exit 1
else
while read line
do
  Y=$(simpleCalc.bash $line)
  ((X=$?))
  if (( X == 0 ))
  then
  echo "$line: $Y" >&1
  else
  echo "$line: Error." >&1
fi
done < $1
fi
exit 0

