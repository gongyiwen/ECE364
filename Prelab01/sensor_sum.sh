#$Author: ee364e03 $
#$Date: 2015-08-31 16:29:38 -0400 (Mon, 31 Aug 2015) $
#$Revision: 80732 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab01/sensor_sum.sh $
#$ID$ 

Param_Values=$@
Num_of_Param=$#

if (($# != 1 ))
then
  echo "Usage: sensor_sum.sh <filename>"
elif [[ ! -r $1 ]]
then
  echo "error:$1 is not a readable file!"
else 
while read line
do
col1=$(echo $line | cut -c 1-2)
col2=$(echo $line | cut -d' ' -f2)
col3=$(echo $line | cut -d' ' -f3)
col4=$(echo $line | cut -d' ' -f4)
((sum=col4+col2+col3))
echo $col1 $sum
done < $1
fi
exit 0
