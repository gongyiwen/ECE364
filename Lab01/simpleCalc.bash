#$Author: ee364e03 $
#$Date: 2015-09-01 15:57:04 -0400 (Tue, 01 Sep 2015) $
#$Revision: 81224 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e03/Lab01/simpleCalc.bash $
#$ID$ 
Num_of_Param=$#
Param_Values=$@
Operator=$1
operand1=$2
operand2=$3
X=0
if (($# != 3 ))
then
  echo "Usage: ./simpleCalc.bash <operator> <operand1> <operand2>"
  exit 1
elif [[ $1 != 'add' && $1 != 'sub' && $1 != 'div' && $1 != 'exp' && $1 != 'mod' && $1 != 'mul' ]]
then
  echo "Error: invalid operator."
  exit 2
else
if [[ $1 == 'add' ]]
then
    ((X=$2+$3))
    echo "$2 + $3 = $X" >&1
elif [[ $1 == 'sub' ]]
  then
    ((X=$2-$3))
    echo "$2 - $3 = $X" >&1
elif [[ $1 == 'div' ]]
then
    ((X=$2/$3))
    echo "$2 / $3 = $X" >&1
elif [[ $1 == 'mul' ]]
  then
    ((X=$2*$3))
    echo "$2 * $3 = $X" >&1
elif [[ $1 == 'exp' ]]
  then
    ((X=$2**$3))
    echo "$2 ^ $3 = $X" >&1
else
    ((X=$2%$3))
    echo "$2 % $3 = $X" >&1
  fi
fi
exit 0






