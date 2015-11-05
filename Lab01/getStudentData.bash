#$Author: ee364e03 $
#$Date: 2015-09-01 17:05:18 -0400 (Tue, 01 Sep 2015) $
#$Revision: 81274 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Lab01/getStudentData.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

exec 3< ./gradebooks/ece337_1.txt
exec 4< ./gradebooks/ece337_2.txt
exec 5< ./gradebooks/ece364_1.txt
exec 6< ./gradebooks/ece364_2.txt
exec 7< ./gradebooks/ece364_3.txt


if (( $# != 1 ))
then
echo "Usage: ./getStudentData.bash <course name>"
exit 1
fi

if [[ $1 != 'ece364' && $1 != 'ece337' ]]
then
echo "Error: course $1 is not a valid option."
exit 2
fi

if [[ $1 == 'ece337' ]]
then
  X1=$(cat ./gradebooks/ece337_1.txt | wc -l)
  X2=$(cat ./gradebooks/ece337_2.txt | wc -l)
  ((Num1=$X1+$X2))
  sum1=0
  highest=0
  name=0
  while read line <&3
  do
  col11=$(echo $line | cut -d',' -f1)
  col12=$(echo $line | cut -d',' -f2)

  if (( col12 > highest ))
  then
     highest=$col12
     name=$col11
  fi
  
  ((sum1=col12+sum1))
  done
  while read line <&4
  do
  col21=$(echo $line | cut -d',' -f1)
  col22=$(echo $line | cut -d',' -f2)
  if (( col22 > highest ))
  then
     highest=$col22
     name=$col21
  fi

  ((sum1=col22+sum1))
  done
  ((average=sum1/Num1))
else
  X3=$(cat ./gradebooks/ece364_1.txt | wc -l)
  X4=$(cat ./gradebooks/ece364_2.txt | wc -l)
  X5=$(cat ./gradebooks/ece364_3.txt | wc -l)
  ((Num1=$X3+$X4+$X5))
  sum1=0
  highest=0
  name=0
  while read line <&5
  do
    col11=$(echo $line | cut -d',' -f1)
    col12=$(echo $line | cut -d',' -f2)
    if (( col12 > highest ))
    then
      highest=$col12
      name=$col11
    fi
   ((sum1=col12+sum1))
  done

  while read line <&6
  do
  col21=$(echo $line | cut -d',' -f1)
  col22=$(echo $line | cut -d',' -f2)
  if (( col22 > highest ))
    then
      highest=$col22
      name=$col21
    fi
  ((sum1=col22+sum1))
  done
  while read line <&7
  do
  col31=$(echo $line | cut -d',' -f1)
  col32=$(echo $line | cut -d',' -f2)
  if (( col32 > highest ))
    then
      highest=$col32
      name=$col31
    fi
  ((sum1=col32+sum1))
  done
  ((average=sum1/Num1))
fi
echo "Total students: $Num1"
echo "Average score: $average"
echo "$name had the highest score of $highest"
exit 0





