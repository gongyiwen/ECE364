#$Author: ee364e03 $
#$Date: 2015-08-30 20:24:33 -0400 (Sun, 30 Aug 2015) $
#$Revision: 80509 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab01/exist.bash $
#$ID$ 
Num_of_Param=$#
Param_Values=$@

while (( $# != 0 ))
do
  if [[ -r $1 ]]
  then
      echo "File $1 is readable!"
  elif [[ ! -r $1 && ! -e $1 ]]
  then
       touch $1
  fi
  shift
done
exit 0
