#! /bin/bash
$Author: ee364e03 $
#$Date: 2015-09-08 16:29:03 -0400 (Tue, 08 Sep 2015) $
#$Revision: 81670 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Lab02/execFiles.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

ls c-files/* > temp
names=$(cut -d'/' -f2 temp)
n=0
name=($names)
if [[ -e namefile ]]
then
  rm namefile
fi
for item in ${name[*]}
do
  printf "%s\n" $item >> namefile
done

nn=$(cut -d'.' -f1 namefile)
nnn=($nn)

while read line
do

if gcc -Wall -Werror ./$line 2>/dev/null
  then
  printf "Attempting to compile %s..." ${name[n]}
  printf " Compilation succeeded.\n"
  ./a.out > ${nnn[n]}.out
else
  printf "Attempting to compile %s..." ${name[n]}
  printf " Error: Compilation failed.\n"
  
fi
((n=n+1))
done < temp

exit 0




