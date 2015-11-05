#$Author: ee364e03 $
#$Date: 2015-08-31 20:13:14 -0400 (Mon, 31 Aug 2015) $
#$Revision: 80848 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab01/line_num.bash $
#$ID$ 

Num_of_Param=$#
Param_Values=$@

if (( $# != 1 ))
then
  echo "User should provide a single argument! "
elif [[ ! -r $1 ]]
then
  echo "Cannot read $1 "
else
X=0
while read line  || [[ -n "$line" ]]
do 
(( X=X+1 ))
echo "$X:$line"
done < $1
fi
exit 0


    
