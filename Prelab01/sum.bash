#$Author: ee364e03 $
#$Date: 2015-08-30 15:58:07 -0400 (Sun, 30 Aug 2015) $
#$Revision: 80390 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Prelab01/sum.bash $
#$ID$ 
Num_of_Param=$#
Param_Values=$@
X=0
while (( $# != 0 ))
do
  ((X=X+$1))
  shift
done
echo ${X}
exit 0


