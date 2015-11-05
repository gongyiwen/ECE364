#! /bin/bash
$Author: ee364e03 $
#$Date: 2015-09-29 17:35:36 -0400 (Tue, 29 Sep 2015) $
#$Revision: 82321 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Lab05/benchmarks.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

Num1=0
Num2=0
n=0
echo -n "Enter the array size(s): "
read  -a input1 < /dev/tty


echo -n "Enter the algorithm(s) to run: "

read  -a input2 < /dev/tty

if [[ -e $1 ]]
then
  rm $1
fi

for item in ${input1[*]}
do
    if (( $item <= 0 ))
then
echo "Error: invalid size of array"
exit 2
fi
done



echo -n "size" >>$1
for item in ${input1[*]}
do
    echo -n ",$item" >> $1
done
   echo "" >>$1
returncode=0
for ((I = 0; I < ${#input2[*]}; I++))
do
  result=()
  for ((W = 0; W < ${#input1[*]}; W++))
  do
    ./sorting ${input1[W]} ${input2[I]} > 1.txt
    result[W]=$(cat 1.txt | tail -c +20)
    returncode=$?
    if (( returncode !=0 ))
    then 
       echo "Error: invalid algorithm name"
       exit 5
    fi
  done
  echo -n "${input2[I]}" >> $1
  for item in ${result[*]}
  do
    echo -n ",$item" >>$1
  done
    echo "" >>$1
done

    
     
	
   


  

   
  
