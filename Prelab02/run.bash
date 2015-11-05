#! /bin/bash
$Author: ee364e03 $
#$Date: 2015-09-05 16:56:08 -0400 (Sat, 05 Sep 2015) $
#$Revision: 81405 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab02/run.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

infilename=$1
outfilename=$2

gcc $1 -o quick_sim
((X=$?))
if (( X != 0 ))
  then
  echo "error: quick_sim could not be compiled!"
  exit 1
fi

while [[ -e $outfilename ]]
do
  echo -n "$outfilename exists. Would you like to delete it? " 
  read input < /dev/tty
  if [[ $input == "y" || $input == "yes" ]]
    then
    rm $outfilename
  elif [[ $input == "n" || $input == "no" ]]
    then
    echo -n "Enter a new filename: "
    read name < /dev/tty
    outfilename=$name
  fi
done

cache=(1 2 4 8 16 32)
issue=(1 2 4 8 16)
fast=99999999
fastname=0
for item1 in ${cache[*]}
do
  for item2 in ${issue[*]}
  do
    X=$(quick_sim $item1 $item2 a)
    CPI=$(echo $X | cut -d' ' -f12)
    CPI1=$(echo $CPI | cut -d':' -f2)
    time=$(echo $X | cut -d' ' -f16)
    time1=$(echo $time | cut -d':' -f2)
    printf "AMD Opteron:%d:%d:%.3f:%d\n" $item1 $item2 $CPI1 $time1 >> $outfilename
    Y=$(quick_sim $item1 $item2 i)
    CPI=$(echo $Y | cut -d' ' -f13)
    CPI2=$(echo $CPI | cut -d':' -f2)
    time=$(echo $Y | cut -d' ' -f17)
    time2=$(echo $time | cut -d':' -f2)
    printf "Intel Core i7:%d:%d:%.3f:%d\n" $item1 $item2 $CPI2 $time2 >> $outfilename
    if (( $time1 < fast ))
    then
      fast=$time1
      fastname="AMD Opeteron"
      fastcache=$item1
      fastissue=$item2
    fi
    if (( $time2 < fast ))
    then
      fast=$time2
      fastname="Intel Core i7"
      fastcache=$item1
      fastissue=$item2
    fi
  done
done
echo "Fastest runtime achieved by $fastname with cache size $fastcache and issue width $fastissue was $fast"
exit 0

        





